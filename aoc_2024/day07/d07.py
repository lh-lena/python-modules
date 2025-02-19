# What is their total calibration result? 3119088655389 
# p2: 3755738907831, 3875816572497 too low

def d07():
    res = 0
    with open("input_3749.txt", "r") as f:
    # with open("input_d07.txt", "r") as f:
        for line in f.readlines():
            key, value = line.split(':')
            if isCorrectSeq(key, value.strip()):
                res += int(key)
    print(res)

def generate_permutations(length):
    if length == 1:
        return ['+', '*']
    permutations = []
    for perm in generate_permutations(length - 1):
        permutations.extend([perm + '+', perm + '*'])
    return permutations


def isCorrectSeq(key: str, value: list) -> bool:
    sum = int(key)
    values = [int(v) for v in value.split()]
    lval = len(values)
    res = 0
    res2 = 0
    permutations = generate_permutations(lval - 1)
    combins = len(permutations) - 1
    i = 1
    while (combins >= 0):
        res = values[0]
        perm = permutations[combins]
        while i < lval:
            l = i
            res2 = values[l]
            concatination = str(res) + str(res2)
            nbr = int(concatination)
            if nbr == sum:
                return True
            l = i + 1
            res2 = nbr
            while l < lval:
                if perm[l - 1] == '+':
                    res2 += values[l]
                elif perm[l - 1] == '*':
                    res2 *= values[l]
                l+=1
            
            if res2 == sum:
                return True
            if perm[i - 1] == '+':
                res += values[i]
            elif perm[i - 1] == '*':
                res *= values[i]
            i += 1
        if res == sum:
            return True
        else:
            i = 1
            res = 0
            combins -= 1
            continue
    return False

if __name__ == "__main__":
    d07()