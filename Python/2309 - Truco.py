forca = {4:1, 5:2, 6:3, 7:4, 12:5, 11:6, 13:7, 1:8, 2:9, 3:10}

N = int(input())

vitorias_adalberto = 0
vitorias_bernardete = 0

for _ in range(N):
    A1, A2, A3, B1, B2, B3 = map(int, input().split())
    pontos_adalberto = 0
    pontos_bernardete = 0

    for a, b in [(A1, B1), (A2, B2), (A3, B3)]:
        if forca[a] >= forca[b]:  
            pontos_adalberto += 1
        else:
            pontos_bernardete += 1

    if pontos_adalberto > pontos_bernardete:
        vitorias_adalberto += 1
    else:
        vitorias_bernardete += 1

print(vitorias_adalberto, vitorias_bernardete)
