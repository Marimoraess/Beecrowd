t = 1
n = int(input())
while n != 0:
    linha = input().split()
    mapa = [
        [linha[0], linha[1]],  # A
        [linha[2], linha[3]],  # B
        [linha[4], linha[5]],  # C
        [linha[6], linha[7]],  # D
        [linha[8], linha[9]],  # E
    ]

    memoria = [None, None, None, None, None, None]
    for i in range(6):
        letra = linha[10 + i]
        indice = ord(letra) - ord("A")
        memoria[i] = mapa[indice]
    for _ in range(n-1):
        linha = input().split()
        mapa = [
            [linha[0], linha[1]],  # A
            [linha[2], linha[3]],  # B
            [linha[4], linha[5]],  # C
            [linha[6], linha[7]],  # D
            [linha[8], linha[9]],  # E
        ]

        for i in range(6):
            letra = linha[10 + i]
            indice = ord(letra) - ord("A")
            par = mapa[indice]
            candidatos = memoria[i]
            candidatos_sobrevivente = []
            for j in range(len(candidatos)):
                if candidatos[j] in par:
                    candidatos_sobrevivente.append(candidatos[j])
            memoria[i] = candidatos_sobrevivente

    print(f"Teste {t}")
    for i in range(6):
        print(memoria[i][0], end=" ")
    print()
    print()

    t += 1
    n = int(input())