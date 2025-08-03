MAX_DIFFERENCE = 3

def solve_day02():
    res = 0
    data = load_input("input_2.txt")
    for line in data:
        if is_valid_line(line, 0):
            print(line)
            res += 1
    print(int(res))

def is_valid_line(sequence, max_corrections):
    numbers = [int(num) for num in sequence]
    
    if len(numbers) < 2:
        return False

    dir = numbers[1] - numbers[0]

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if  (dir >= 0 and (diff <= 0 or diff > MAX_DIFFERENCE)) or \
            (dir <= 0 and (diff >= 0 or diff < -MAX_DIFFERENCE)):
            if (max_corrections < 1):
                if dir >= diff:
                    del numbers[i-1]
                else:
                    del numbers[i]
                    
                return is_valid_line(numbers, max_corrections+1)
            return False
    
    return True

def load_input(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip().replace(" ", "") for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found")
        return []



if __name__ == "__main__":
    solve_day02()

# part1 too high: 482
# part2 too low: 360