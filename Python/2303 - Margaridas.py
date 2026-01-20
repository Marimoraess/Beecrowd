L, C, M, N = map(int, input().split())

plantacao = []
for _ in range(L):
    linha = list(map(int, input().split()))
    plantacao.append(linha)

maior = 0


for i in range(0, L, M):
    for j in range(0, C, N):
        soma = 0
        for x in range(i, i + M):
            for y in range(j, j + N):
                soma += plantacao[x][y]
        if soma > maior:
            maior = soma

print(maior)
