N, C = map(int, input().split())
ocupacao = 0
excedeu = False

for _ in range(N):
    S, E = map(int, input().split())
    ocupacao -= S
    ocupacao += E
    if ocupacao > C:
        excedeu = True
        break

print('S' if excedeu else 'N')
