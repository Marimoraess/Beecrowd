while True:
    X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        break
    distancia = bin(X ^ Y).count('1')
    print(distancia)
