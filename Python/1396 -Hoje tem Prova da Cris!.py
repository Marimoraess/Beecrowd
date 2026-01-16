inst = 1
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    nomes = input().split()

    for i in range(n):
        limite = min(n - 1, i + k)

        pos_menor = i
        for j in range(i + 1, limite + 1):
            if nomes[j] < nomes[pos_menor]:
                pos_menor = j

        custo = pos_menor - i

        # puxar
        while pos_menor > i:
            nomes[pos_menor], nomes[pos_menor - 1] = nomes[pos_menor - 1], nomes[pos_menor]
            pos_menor -= 1

        k -= custo
        if k <= 0:
            break

    print(f"Instancia {inst}")

    # imprime com espaço após o último
    for nome in nomes:
        print(nome, end=" ")
    print()     
    print()     

    inst += 1
