while True:
    linha = input()
    if not linha:
        continue
    N, M = map(int, linha.split())
    if N == 0 and M == 0:
        break

    P = [0] + list(map(int, input().split())) 

    parent = [i for i in range(N+1)]
    soma = P[:]  

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def unite(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[b] = a
            soma[a] += soma[b]

    rafael = 1
    vit = 0

    for _ in range(M):
        acoes = input().split()
        if not acoes:
            continue
        q, a, b = map(int, acoes)
        if q == 1:
            unite(a, b)
        else:
            ra = find(a)
            rb = find(b)
            rr = find(rafael)
            if ra == rb:
                continue
            if rr == ra:
                if soma[ra] > soma[rb]:
                    vit += 1
            elif rr == rb:
                if soma[rb] > soma[ra]:
                    vit += 1

    print(vit)
