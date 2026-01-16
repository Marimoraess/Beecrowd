quantidade = int(input())
for i in range(quantidade):
    palavra = input()
    quant_posicoes = int(input())
    resposta = ''
    for j in palavra:
        letra = ord(j) - quant_posicoes
        if letra < 65:
            resposta += chr(91-(65-letra))
        else:
            resposta += chr(letra)
    print(resposta)