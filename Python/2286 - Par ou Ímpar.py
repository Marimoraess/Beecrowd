teste = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    jogador1 = input().strip()
    jogador2 = input().strip()
    
    print(f"Teste {teste}")
    for _ in range(N):
        A, B = map(int, input().split())
        soma = A + B
        if soma % 2 == 0:
            print(jogador1)
        else:
            print(jogador2)
    
    print()  
    teste += 1
