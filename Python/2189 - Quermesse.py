t = 0
while True:
    n = int(input())
    if n == 0:
        break
    t += 1
    linha = list(map(int, input().split()))
    
    for c in range(n):
        if linha[c] == c + 1:
            print(f'Teste {t}')
            print(linha[c])
            print()
            