N, numero = input().split()
lista = []
while N != '0' and numero != '0':
    resposta = ''
    for i in range(len(numero)):
        lista.append(numero[i])
    for c in range(len(lista)):
        if lista[c] != N:
            resposta += lista[c]
    if resposta != '':
        resposta = int(resposta)
        if resposta < 1:
            print("0")
        else:
            print(resposta)
    else:
        print('0')
    N, numero = input().split()
    lista = []