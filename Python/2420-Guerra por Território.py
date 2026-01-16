n = int(input())
dados = list(map(int,input().split()))
lista_soma = []
aux = 0
for i in range(n):
    soma = dados[i] + aux
    aux = soma
    lista_soma.append(soma)

for j in range(n):
    if lista_soma[j] == lista_soma[-1] - lista_soma[j]:
        pos = j+1
print(pos)