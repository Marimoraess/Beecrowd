while True:
    try:
        linhas, colunas = map(int,input().split())
        matriz = []
        soma = 0
        for i in range(linhas):
            matriz.append(list(map(int,input().split())))
            for j in range(len(matriz[i])):
                soma += matriz[i][j]
        sacas = soma // 60
        litros = soma % 60
        print(f"{sacas} saca(s) e {litros} litro(s)")

    except EOFError:
        break