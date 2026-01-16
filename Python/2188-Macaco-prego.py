regioes = int(input())
teste = 1
while regioes != 0:
    xs = []
    ys = []
    us = []
    vs = []

    for i in range(regioes):
        dados = list(map(int,input().split()))
        xs.append(dados[0])
        ys.append(dados[1])
        us.append(dados[2])
        vs.append(dados[3])
        
    x = max(xs)
    y = min(ys)
    u = min(us)
    v = max(vs)

    print(f"Teste {teste}")
    teste += 1

    if x<u and y>v:
        print(f"{x} {y} {u} {v}")
    else:
        print('nenhum')
    print()

    regioes = int(input())