barras = int(input())
matriz = []

for i in range(barras):
    matriz.append(input())
matriz.sort(reverse=True, key=len)
strings = []
i = 0
for j in range(len(matriz[0])):
    resp = 0
    for outras_barras in range(1, barras):
        if matriz[0][i:j+1] in matriz[outras_barras]:
            resp += 1
        else:
            break
    if resp == barras - 1:
        string = matriz[0][i:j+1]
        if string != '':
            strings.append(string)
    else:
        i += 1
strings.sort(reverse=True, key=len)
print(strings[0])

