N = int(input())

quadrado = [list(map(int, input().split())) for _ in range(N)]

soma_alvo = sum(quadrado[0])

magico = True

for i in range(N):
    if sum(quadrado[i]) != soma_alvo:
        magico = False
        break

if magico:
    for j in range(N):
        if sum(quadrado[i][j] for i in range(N)) != soma_alvo:
            magico = False
            break

if magico:
    if sum(quadrado[i][i] for i in range(N)) != soma_alvo or sum(quadrado[i][N-1-i] for i in range(N)) != soma_alvo:
        magico = False

print(soma_alvo if magico else -1)
