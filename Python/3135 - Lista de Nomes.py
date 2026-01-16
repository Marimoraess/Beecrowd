n = int(input())
names = []
for _ in range(n):
    names.append(input().strip())

groups = {}
for name in names:
    t = len(name)
    if t not in groups:
        groups[t] = []
    groups[t].append(name)

sizes = sorted(groups.keys())

max_len = 0
for t in sizes:
    if len(groups[t]) > max_len:
        max_len = len(groups[t])

for i in range(max_len):
    line = []
    for t in sizes:
        if i < len(groups[t]):
            line.append(groups[t][i])
    print(", ".join(line))
