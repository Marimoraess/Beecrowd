
N = int(input())


if N == 1:
    input()
    print(1)
else:

    sequencia = list(map(int, input().split()))


    escadinhas = 1
    
    diferenca_atual = sequencia[1] - sequencia[0]


    for i in range(2, N):
     
        nova_diferenca = sequencia[i] - sequencia[i-1]
        
    
        if nova_diferenca != diferenca_atual:
            escadinhas += 1
            diferenca_atual = nova_diferenca
            
    print(escadinhas)