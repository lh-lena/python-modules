

def d05():

    res = 0
    res2 = 0
    order = []
    pages = []
    # with open("input_143.txt", "r") as f:
    with open("input_d05.txt", "r") as f:
        for line in f.readlines():
            if '|' in line:
                order.append(line.strip().split('|'))
            elif line != "\n":
                pages.append(line.strip().split(','))
    
    for page in pages:
        if isCorrectOder(page, order):
            mid = len(page) // 2
            res += int(page[mid])
        if getIncorrectOrder(page, order):
            toCorrect(page, order)
            mid = len(page) // 2
            res2 += int(page[mid])
    print(res2)

def toCorrect(page: list, order: list):
    lpage = len(page)
    current_pair = []
    for i in range(lpage - 1):
        current_pair.append(page[i])
        current_pair.append(page[i+1])
        # print(current_pair)
        if current_pair not in order:
            swap_elements(page, i, i+1)
            toCorrect(page, order)
        current_pair.clear()

def isCorrectOder(page: list, order: list):
    t = 0
    current_pair = []
    lpage = len(page)
    for i in range(lpage - 1):
        current_pair.append(page[i])
        current_pair.append(page[i+1])
        # print(current_pair)
        if current_pair in order:
            t += 1
        current_pair.clear()
    t+=1
    if t == lpage:
        return True
    return False

def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def getIncorrectOrder(page: list, order: list):
    current_pair = []
    lpage = len(page)
    for i in range(lpage - 1):
        current_pair.append(page[i])
        current_pair.append(page[i+1])
        # print(current_pair)
        if current_pair not in order:
            return page
        current_pair.clear()
    return []


if __name__ == "__main__":
    d05()

# 4996
#part2 -> 6311

"""
Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.

The second and third updates are also in the correct order according to the rules. Like the first update, they also do not include every page number, and so only some of the ordering rules apply - within each update, the ordering rules that involve missing page numbers are not used.

The fourth update, 75,97,47,61,53, is not in the correct order: it would print 75 before 97, which violates the rule 97|75.

The fifth update, 61,13,29, is also not in the correct order, since it breaks the rule 29|13.

The last update, 97,13,75,29,47, is not in the correct order due to breaking several rules.

For some reason, the Elves also need to know the middle page number of each update being printed. Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:

75,47,61,53,29
97,61,53,29,13
75,29,13

Part2:
For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
"""