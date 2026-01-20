I, N = map(int, input().split())

# saldos iniciais
D = E = F = I

for _ in range(N):
    op = input().split()
    
    if op[0] == 'C':  # Compra
        J, X = op[1], int(op[2])
        if J == 'D':
            D -= X
        elif J == 'E':
            E -= X
        else:
            F -= X

    elif op[0] == 'V':  # Venda
        J, X = op[1], int(op[2])
        if J == 'D':
            D += X
        elif J == 'E':
            E += X
        else:
            F += X

    else:  # Aluguel
        J, K, X = op[1], op[2], int(op[3])
        # J recebe
        if J == 'D':
            D += X
        elif J == 'E':
            E += X
        else:
            F += X
        # K paga
        if K == 'D':
            D -= X
        elif K == 'E':
            E -= X
        else:
            F -= X

print(D, E, F)
