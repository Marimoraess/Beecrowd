N, M = map(int, input().split())

problemas = []

for _ in range(N):
    linha = input().split()
    for item in linha:
        criticidade = int(item[0])
        tipo = item[1]
        problemas.append((tipo, criticidade, item))

problemas.sort(key=lambda x: (x[0] == 'D', -x[1]))

for p in problemas:
    print(p[2])
