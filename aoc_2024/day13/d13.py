#! /usr/bin/env python3

'''
To press a button costs:
A = 3 
B = 1 
A:     X*n Y*n
B:     X*m Y*m
Price: X=x Y=y

A: 94*80 34*80
B: 22*40 67*40
   8400  5400

A and B must be pressed no more 100 time
'''

def d13():
    res = 0
    data = []

    with open("input.txt", "r") as f:
    # with open("input_day13.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if (line and (line.find("A") != -1 or line.find("B") != -1)):
                posX = line.find("X+") + 2
                posY = line.find("Y+") + 2
                data.append((line[posX:posX+2], line[posY:]))
            elif (line):
                pos_x = line.find("X=") + 2
                pos_y = line.find(", Y=")
                data.append((line[pos_x:pos_y], line[pos_y + 4:]))
    print(data)
    res = 0
    for i in range(0, len(data)-1, 3):
        res1 = 0
        res2 = 0
        x1, y1 = data[i]
        x2, y2 = data[i+1]
        x, y = data[i+2]
        n = 1
        m = 1
        while True:
            if n >= 10:
                break
            if m >= 10:
                break
            ratio = (int(x1) + int(y1)) * int(n) - (int(x2) + int(y2)) * int(m)
            left = (int(y) + 1) * int(int(y1) * int(n) + int(y2) * int(m))
            rigth = (int(x) + 1) *  int(int(x1) * int(n) + int(x2) * int(m))
            print("n : ", n, " m : ", m)
            print(left, rigth)
            print(left - rigth)
            print("ratio", ratio)
            if (left == rigth):
                print("Equal")
            elif (left > rigth):
                # n += 1
                if ratio > 0:
                    m += 1
                else:
                    n += 1
            elif (left < rigth):
                if ratio < 0:
                    n += 1
                else:
                    m += 1
        
        # res1 = calc_steps(x1, x2, x)
        # res2 = calc_steps(y1, y2, y)
        # print("res: ", res1, res2)
        # if res1 == -1 or res2 == -1:
        #     continue
        # res += (res1 + res2)
    print(res)


# def calc_steps(A, B, sum):
#     a = 0
#     b = 0
#     res = 0
    

if __name__ == "__main__":
    d13()
