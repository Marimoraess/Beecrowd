L = input().split()         # lista atual
N = input().split()         # nova lista
S = input().strip()         # amigo que receberá indicação

if S != "nao" and S in L:
    pos = L.index(S)
    # insere N antes de S
    L = L[:pos] + N + L[pos:]
else:
    # adiciona no final
    L = L + N

print(" ".join(L))
