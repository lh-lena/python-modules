

import re

def inDoRange(pos, do_positions, dont_positions):
    
    prev_dont = max([d for d in dont_positions if d <= pos], default=0)

    if not prev_dont:
        return True 
    for do_pos in do_positions:
        if do_pos > prev_dont and do_pos <= pos:
            return True

    return False

def d03():
    with open("input.txt", "r") as f:
        content = f.read()
        res = 0
        data = re.finditer(r'mul\(\d+,\d+\)', content)
        dont_positions = [m.start() for m in re.finditer(r"don't\(\)", content)]
        do_positions = [m.start() for m in re.finditer(r"(?<!don\'t\()\s*do\(\)", content)]
        fil = []
        for match in data:
            try:
                start_index = match.start()
                
                if inDoRange(start_index, do_positions, dont_positions):
                    fil.append(match.group())
            except IndexError:
                continue
        for el in fil:
            if el:
                d = el[4:-1].split(",")
                if (abs(int(d[0])) > 999 or abs(int(d[1])) > 999):
                    continue
                res += (int(d[0]) * int(d[1]))
    print(res)

if __name__ == "__main__":
    d03()

#175015740 part1
#112272912 part2