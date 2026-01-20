n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

row = [sum(mat[i]) for i in range(n)]
col = [sum(mat[i][j] for i in range(n)) for j in range(n)]
em
if row[0] == row[1] or row[0] == row[2 if n > 2 else 1]:
    M = row[0]
else:
    M = row[1]

for i in range(n):
    if row[i] != M:
        L = i
        break

for j in range(n):
    if col[j] != M:
        C = j
        break

alterado = mat[L][C]


dif = row[L] - M

l
original = alterado - dif

print(original, alterado)
