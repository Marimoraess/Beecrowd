from operator import itemgetter

N = int(input())

paises = []

for _ in range(N):
    entrada = input().split()
    nome = entrada[0]
    ouro, prata, bronze = map(int, entrada[1:])
    paises.append((nome, ouro, prata, bronze))

paises.sort(key=itemgetter(0))


paises.sort(key=itemgetter(3), reverse=True)
paises.sort(key=itemgetter(2), reverse=True)
paises.sort(key=itemgetter(1), reverse=True)

for p in paises:
    print(p[0], p[1], p[2], p[3])
