N, Q = map(int, input().split())
vetor = list(map(int, input().split()))

for _ in range(Q):
    L, R, K, G, D = map(int, input().split())
    L -= 1
    R -= 1
    intervalo = vetor[L:R+1]
    intervalo.sort()
    k_esimo = intervalo[K-1]
    freq = intervalo.count(k_esimo)
    if abs(freq - G) < abs(freq - D):
        vencedor = 'G'
    elif abs(freq - G) > abs(freq - D):
        vencedor = 'D'
    else:
        vencedor = 'E'
    print(f"{k_esimo} {freq} {vencedor}")
