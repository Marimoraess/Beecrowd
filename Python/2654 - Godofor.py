N = int(input())

candidatos = []

for _ in range(N):
    entrada = input().split()
    nome = entrada[0]
    P, K, M = map(int, entrada[1:])
    candidatos.append(( -P, -K, M, nome ))  # Negativos para ordenar decrescente

candidatos.sort()

print(candidatos[0][3])
