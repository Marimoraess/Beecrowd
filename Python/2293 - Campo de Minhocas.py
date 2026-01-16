N, M = map(int, input().split())

campo = []
for _ in range(N):
    linha = list(map(int, input().split()))
    campo.append(linha)

maior_soma = 0

for i in range(N):
    soma_linha = sum(campo[i])
    if soma_linha > maior_soma:
        maior_soma = soma_linha


for j in range(M):
    soma_coluna = 0
    for i in range(N):
        soma_coluna += campo[i][j]
    if soma_coluna > maior_soma:
        maior_soma = soma_coluna

print(maior_soma)