with open(r"aoc22_1_input") as f:
    data = f.readlines()

result = list()

sum_ = 0
for row in data:
    row = row.strip()
    if row != '':
        sum_ += int(row)
        continue;
    result.append(sum_)
    sum_ = 0   
    
print(max(result))

print(sum((sorted(result, reverse=True)[0:3])))

