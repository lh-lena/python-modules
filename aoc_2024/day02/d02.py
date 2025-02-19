

def d02():
    res = 0
    # with open("input_2.txt", "r") as f:
    with open("input_d02.txt", "r") as f:
        data = [line.strip().replace(" ", "") for line in f.readlines()]
    for line in data:
        if is_valid_line(line, 0):
            print(line)
            res += 1
    print(int(res))

def is_valid_line(line, k):
    numbers = [int(num) for num in line]
    
    if len(numbers) < 2:
        return False
    
    dir = numbers[1] - numbers[0]
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if (dir >= 0 and (diff <= 0 or diff > 3)) or (dir <= 0 and (diff >= 0 or diff < -3)):
            if ( k < 1):
                if dir >= diff:
                    del numbers[i-1]
                else:
                    del numbers[i]
                    
                return is_valid_line(numbers, k+1)
            return False
    
    return True



if __name__ == "__main__":
    d02()

# part1 too high: 482
# part2 too low: 360