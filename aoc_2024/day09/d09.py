#!/usr/bin/env python3
# P1: 6301895872542 
# to0 hight 6399865217220 6399865217220
# test input: 1928
# 49709 files -> res 49710

def d09():
    with open("input.txt", "r") as f:
    # with open("input_d09.txt", "r") as f:
        context = f.read()
    parsed = parse_disk_map(context)
    # detailed_map = build_detailed_map(parsed)
    # final_state = move_blocks(detailed_map)
    # res = 0
    # for i in range(len(final_state)):
    #     res += (i * final_state[i])
    # print(res)
    
    # part 2
    print(print_2_part(move_whole_blocks(build_map_pairs(parsed))))

def parse_disk_map(disk_map):
    """
    Parse the dense disk map input into a structured list of file and free space lengths.
    """
    parsed = []
    for block in range(0, len(disk_map), 2):
        file_len = int(disk_map[block])
        free_len = int(disk_map[block + 1]) if block + 1 < len(disk_map) else 0
        parsed.append((file_len, free_len))
    return parsed

def build_detailed_map(parsed):
    """
    Build the detailed disk map as a list of characters based on file and free space lengths.
    """
    detailed_map = []
    file_id = 0
    for file_len, free_len in parsed:
        for i in range(file_len):
            detailed_map.append(file_id)
        for j in range(free_len):
            detailed_map.append(-1)
        file_id += 1
    return detailed_map

def move_blocks(detailed_map):
    """
    Move file blocks to fill gaps, one block at a time.
    """

    for i in range(len(detailed_map) - 1, 0, -1):
        if detailed_map[i] != -1:
            # swap elements
            try:
                idx = detailed_map.index(-1)
                if idx == i:
                    return detailed_map
                detailed_map[idx], detailed_map[i] = detailed_map[i], detailed_map[idx]
                # print(detailed_map)
                del detailed_map[i]
            except ValueError:
                return detailed_map
        elif detailed_map[i] == -1:
            del detailed_map[i]
    return detailed_map

def build_map_pairs(parsed):
    """
    Build the detailed disk map as a list of characters based on file length and its ID number and free space length
    """
    detailed_map = []
    file_id = 0
    for file_len, free_len in parsed:
        detailed_map.append((file_len, file_id))
        if free_len != 0:
            detailed_map.append((free_len, -1))
        file_id += 1
    return detailed_map


    """TODO
    - to change logic to search for an empty place for highest ID
    """
# def move_whole_blocks(detailed_map: list):
#     """
#     Move file blocks to fill gaps, whole block at a time if can fit in space span
#     """
#     print(detailed_map, "\n Start")
#     n = 0
#     while n < len(detailed_map):
#         if (detailed_map[n] == None):
#             n += 1
#             continue
#         if n >= len(detailed_map):
#             detailed_map = [el for el in detailed_map if el is not None]
#             print(detailed_map)
#             return detailed_map
#         el_left, el_right = detailed_map[n]
#         if el_right != -1:
#             n+=1
#             continue
#         del detailed_map[n]
#         for i in range(len(detailed_map) - 1, 0, -1):
#             if (n == i or i < 0):
#                 break
#             if  detailed_map[i] == None:
#                 i-=1
#                 continue
#             el_l, el_r = detailed_map[i]
#             if el_r != -1:
#                 if (el_l > el_left):
#                     i -= 1
#                     continue
#                 detailed_map.insert(n, detailed_map[i])
#                 detailed_map[i+1] = (el_l, -1)
#                 if (el_left - el_l > 0):
#                     tmp = (el_left - el_l, el_right)
#                     detailed_map.insert(n+1, tmp)
#                 n -= 1
#                 # print(detailed_map)
#                 break
#         n += 1
#     # print(detailed_map)
#     detailed_map = [el for el in detailed_map if el is not None]
#     return detailed_map


def move_whole_blocks(detailed_map: list):
    """
    Move file blocks to fill gaps, whole block at a time if can fit in space span
    """
    map_len = len(detailed_map)
    for n in range(map_len - 1, 0, -1):
        el_left, el_right = detailed_map[n]
        if el_right == -1:
            continue
        for i in range(map_len):
            if (n == i):
                break
            el_l, el_r = detailed_map[i]
            if el_r == -1:
                if (el_left > el_l):
                    continue
                detailed_map.insert(i, detailed_map[n])
                # update_empty_space(detailed_map, n+1, el_left, map_len)
                detailed_map[n+1] = (el_left, el_r)
                if (el_l - el_left > 0):
                    # update_empty_space(detailed_map, i+1, el_l - el_left, map_len)
                    detailed_map[i+1] = (el_l - el_left, el_r)
                elif (el_l - el_left == 0):
                    del detailed_map[i+1]
                break
    print(detailed_map)
    return detailed_map

def update_empty_space(detailed_map, cur_idx, val, max_idx):
    if cur_idx + 1 < max_idx:
        el1, el2 = detailed_map[cur_idx + 1]
        if el2 == -1:
            val += el1
            del detailed_map[cur_idx + 1]
        detailed_map[cur_idx] = (val, -1)
    if cur_idx - 1 >= 0:
        el_l, el_r = detailed_map[cur_idx - 1]
        if el_r != -1:
            detailed_map[cur_idx] = (val, -1)
            return
        val += el_l
        detailed_map[cur_idx] = (val, -1)
        del detailed_map[cur_idx - 1]

def print_2_part(detailed_map):
    size = 0
    for i, (el_left, el_right) in enumerate(detailed_map):
        size += el_left
    res = 0
    k = 0
    for i, (el_left, el_right) in enumerate(detailed_map):
        if (k >= size):
            return res
        if el_right == -1:
            for t in range(el_left):
                k += 1
            continue
        for n in range(el_left):
            res += k * el_right
            k += 1
    return res



if __name__ == "__main__":
    d09()