wins_against = {
    "X": "C", 
    "Y": "A",
    "Z": "B",
    "A": "Z", 
    "B": "X",
    "C": "Y" }

eq_map = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

pts_key = {
    "X": 1,
    "Y": 2,
    "Z": 3 }

outcome_key = {
    "X": "lose",
    "Y": "draw",
    "Z": "win" }

with open(r"aoc22_2_input") as f:
    data = f.readlines()


t = 0

for line in data:
    x, y = line.split()

    x = ord(x) - 65

    if y == "X":
        t += (x - 1) % 3 + 1
    elif y == "Y":
        t += 3 + x + 1
    else:
        t += 6 + (x + 1) % 3 + 1

print(t)

# result = 0

# for row in data:
#     opponent, you = row.split()

#     if outcome_key[you] == "lose":
#         # Lose
#         you = wins_against[opponent]
#         result += pts_key[you]
#     elif outcome_key[you] == "win":
#         # Win
#         temp = wins_against[you]
#         you = wins_against[temp]
#         result += pts_key[you] + 6
#     else:
#         # Draw
#         you = eq_map[opponent]
#         r = pts_key[you] + 3
#         result += r

#     # if wins_against[opponent] == you:
#     #     result += pts_key[you]
#     # elif wins_against[you] == opponent:
#     #     result += pts_key[you] + 6
#     # else:
#     #     result += pts_key[you] + 3

# print(result)