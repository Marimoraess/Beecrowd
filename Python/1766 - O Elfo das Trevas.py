testes = int(input())
for teste in range(testes):
    total, puxar = map(int,input().split())
    matriz = []
    for j in range(total):
        matriz.append(input().split())
        matriz[j][1] = int(matriz[j][1])
        matriz[j][2] = int(matriz[j][2])
        matriz[j][3] = float(matriz[j][3])
    print('CENARIO {' + str(teste+1) + '}')
        
    for x in range(len(matriz)-1):
        for y in range(len(matriz)-1):
            if matriz[y][1] < matriz[y+1][1]:
                aux = matriz[y]
                matriz[y] = matriz[y+1]
                matriz[y+1] = aux
            elif matriz[y][1] == matriz[y+1][1]:
                if matriz[y][2] > matriz[y+1][2]:
                    aux = matriz[y]
                    matriz[y] = matriz[y+1]
                    matriz[y+1] = aux
                elif matriz[y][2] == matriz[y+1][2]:
                    if matriz[y][3] > matriz[y+1][3]:
                        aux = matriz[y]
                        matriz[y] = matriz[y+1]
                        matriz[y+1] = aux
    for numero in range(puxar):
        resultado = matriz[numero][0]
        print(f"{numero+1} - {resultado}")