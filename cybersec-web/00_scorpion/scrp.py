import exifread


def scrp(data: list):
    parse_and_modify_exif(read_binary(data[0]))
    return


def locate_exif_segment(binary_data):
    offset = 0
    while offset < len(binary_data):
        # Look for APP1 marker (0xFFE1)
        print(binary_data[offset:offset+2])
        if binary_data[offset:offset+2] == b'\xFF\xE1':
            # Read length of the segment
            length = int.from_bytes(binary_data[offset+2:offset+4], "big")
            # Check for EXIF marker
            if binary_data[offset+4:offset+10] == b'Exif\x00\x00':
                return offset + 10, length - 8  # Start of EXIF data
        offset += 2  # Move to the next marker
    raise ValueError("EXIF data not found")

def parse_exif_data(binary_data, exif_offset):
    # Read endianness
    endianness = binary_data[exif_offset:exif_offset+2]
    if endianness == b'II':
        byte_order = "little"
    elif endianness == b'MM':
        byte_order = "big"
    else:
        raise ValueError("Invalid TIFF header")

    # Read the offset to the first IFD
    ifd_offset = int.from_bytes(binary_data[exif_offset+4:exif_offset+8], byte_order)

    # Read and parse IFD
    tags = {}
    current_offset = exif_offset + ifd_offset
    num_entries = int.from_bytes(binary_data[current_offset:current_offset+2], byte_order)
    current_offset += 2

    for _ in range(num_entries):
        tag_id = int.from_bytes(binary_data[current_offset:current_offset+2], byte_order)
        tag_type = int.from_bytes(binary_data[current_offset+2:current_offset+4], byte_order)
        value_count = int.from_bytes(binary_data[current_offset+4:current_offset+8], byte_order)
        value_offset = int.from_bytes(binary_data[current_offset+8:current_offset+12], byte_order)
        tags[tag_id] = (tag_type, value_count, value_offset)
        current_offset += 12

    return tags

def read_binary(file_path):
    with open(file_path, "rb") as f:
        return f.read()

def write_binary(file_path, binary_data):
    with open(file_path, "wb") as f:
        f.write(binary_data)


def parse_and_modify_exif(binary_data):

    # Locate EXIF data
    try:
        exif_offset, exif_length = locate_exif_segment(binary_data)
        print(f"EXIF data found at offset {exif_offset}, length {exif_length}")
    except ValueError as e:
        print(e)
        return

    # Parse EXIF data
    tags = parse_exif_data(binary_data, exif_offset)
    print("EXIF Tags:", tags)

    # Example modification: Replace a tag value (not implemented in detail here)
    # You can modify the binary_data directly or rebuild the EXIF segment.

    # Write modified data to a new file
    # write_binary(output_path, binary_data)
    # print(f"Modified file saved to {output_path}")

def parse_jpeg(file_path):
    data = read_binary(file_path)
    i = 2  # Start after the SOI marker
    print(len(data))
    while i < len(data):
        # JPEG segment starts with 0xFF and is followed by the segment type
        if data[i] == 0xFF:
            marker = data[i + 1]
            print(f"Found marker: 0x{marker:02X}")
            
            # Some segments are variable in size (e.g., APP0, APP1 for EXIF)
            # Get the length of the segment
            length = int.from_bytes(data[i + 2:i + 4], byteorder='big')
            
            print(f"Segment length: {length}")
            
            # Move the pointer to the next segment
            i += 2 + length
        else:
            # If we don't find a valid marker, break the loop
            break
    
    # Check for the End of Image (EOI) marker (0xFFD9)
    if data[-2:] == b'\xFF\xD9':
        print("End of Image (EOI) found")
    else:
        print(len(data[i:]))
        parse_and_modify_exif(data[i:])
        # print("No End of Image (EOI) marker found")
