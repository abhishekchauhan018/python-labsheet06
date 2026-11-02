from itertools import combinations

s = {1, 2, 3}
power_set = []

for i in range(len(s) + 1):
    for j in combinations(s, i):
        power_set.append(set(j))

print("Power Set:", power_set)