The second scorpion program receive image files as parameters and must be able to
parse them for EXIF and other metadata, displaying them on the screen.
The program must at least be compatible with the same extensions that spider handles.
It display basic attributes such as the creation date, as well as EXIF data. The output format is up to you.

Usage:
    ./scorpion FILE1 [FILE2 ...]

JPEG starts with b'\xFF\xD8' (hexadecimal FFD8).
PNG starts with b'\x89PNG\r\n\x1a\n'