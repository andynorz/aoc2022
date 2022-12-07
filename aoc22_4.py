with open(r"aoc22_4_input") as f:
    data = f.readlines()

overlaps = 0
intersects = 0

for line in data:
    first, second = line.strip().split(",")
    start_f, end_f = first.split("-")
    start_s, end_s = second.split("-")

    start_f = int(start_f)
    start_s = int(start_s)
    end_f = int(end_f)
    end_s = int(end_s)

    fs = set(range(start_f, end_f + 1))
    ss = set(range(start_s, end_s + 1))

    if fs.issubset(ss) or ss.issubset(fs):
        overlaps += 1

    if intersect := fs.intersection(ss):
        intersects += 1

print(overlaps)
print(intersects)
