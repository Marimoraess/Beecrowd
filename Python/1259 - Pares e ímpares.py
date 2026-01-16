n = int(input())
pares = []
impar = []

for c in range(n):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)

pares.sort()
impar.sort(reverse=True)

for p in pares:
    print(p)

for i in impar:
    print(i)
