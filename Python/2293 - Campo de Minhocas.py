linhas, colunas = map(int, input().split())

matriz = []
for _ in range(linhas):
    valores = list(map(int, input().split()))
    matriz.append(valores)

max_soma = 0

for i in range(linhas):
    soma_l = sum(matriz[i])
    if soma_l > max_soma:
        max_soma = soma_l


for j in range(colunas):
    soma_c = 0
    for i in range(linhas):
        soma_c += matriz[i][j]
    if soma_c > max_soma:
        max_soma = soma_c

print(max_soma)
