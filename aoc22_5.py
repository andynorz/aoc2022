import re


def move_to(fr, to, how_many):
    fr = fr - 1
    to = to - 1
    # Pop normal way
    # for i in range(how_many):
    #     popped = el_stacko[fr].pop()
    #     el_stacko[to].extend(popped)

    # Pop inplace
    popped = el_stacko[fr][-how_many:]
    del el_stacko[fr][-how_many:]
    el_stacko[to].extend(popped)


with open(r"aoc22_5_input") as f:
    data = f.readlines()

el_stacko = [[], [], [], [], [], [], [], [], []]

for row in data[7::-1]:
    for j in range(9):
        char = row[j*4 + 2 - 1]
        if char != " ":
            el_stacko[j].append(char)

print(el_stacko)

for instruction in data[10:]:
    num, from_, to = re.findall(r"\d+", instruction)
    move_to(int(from_), int(to), int(num))

print(".-------------")
print(el_stacko)
print("".join(stack[-1] for stack in el_stacko))
