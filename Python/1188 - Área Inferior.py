op = input().strip()

mat = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    mat.append(linha)

soma = 0.0
qtd = 0

for i in range(7, 12):  
    for j in range(12 - i, i):  
        qtd += 1

if op == 'S':
    print(f"{soma:.1f}")
else:
    print(f"{(soma / qtd):.1f}")
