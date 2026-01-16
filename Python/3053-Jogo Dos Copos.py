n = int(input())
copo = input()
if copo == 'A':
    lista = [1,0,0]
elif copo == 'B':
    lista = [0,1,0]
else:
    lista = [0,0,1]
for i in range(n):
    jogada = input()
    if jogada == '1':
        aux = lista[0]
        lista[0] = lista[1]
        lista[1] = aux
    elif jogada == '2':
        aux = lista[1]
        lista[1] = lista[2]
        lista[2] = aux
    else:
        aux = lista[0]
        lista[0] = lista[2]
        lista[2] = aux
if lista[0] == 1:
    print('A')
elif lista[1] == 1:
    print('B')
else:
    print('C')