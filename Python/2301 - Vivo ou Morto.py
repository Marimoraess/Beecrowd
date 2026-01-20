teste = 1

while True:
    P, R = map(int, input().split())
    if P == 0 and R == 0:
        break

    fila = list(map(int, input().split()))

    for _ in range(R):
        dados = list(map(int, input().split()))
        N = dados[0]
        ordem = dados[1]
        acoes = dados[2:]

        nova_fila = []
        for i in range(N):
            if acoes[i] == ordem:
                nova_fila.append(fila[i])

        fila = nova_fila

    print(f"Teste {teste}")
    print(fila[0])
    print()
    teste += 1
