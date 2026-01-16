casos = int(input())
for j in range(casos):
    A,B = input().split()
    if len(B) <= len(A):
        posicao = 1
        cont = 0
        for i in range(len(B)):
            if B[-posicao] == A[-posicao]:
                cont += 1
            posicao += 1
        if cont == len(B):
            resposta = 'encaixa'
        else:
            resposta = 'nao encaixa'
    else:
        resposta = 'nao encaixa'
    
    print(resposta)