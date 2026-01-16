valor = float(input())
valor = int(round(valor * 100))

notas = [0, 0, 0, 0, 0, 0]
moedas = [0, 0, 0, 0, 0, 0]

while valor != 0:
    if valor >= 10000:
        notas[0] = valor // 10000
        valor %= 10000
    elif valor >= 5000:
        notas[1] = valor // 5000
        valor %= 5000
    elif valor >= 2000:
        notas[2] = valor // 2000
        valor %= 2000
    elif valor >= 1000:
        notas[3] = valor // 1000
        valor %= 1000
    elif valor >= 500:
        notas[4] = valor // 500
        valor %= 500
    elif valor >= 200:
        notas[5] = valor // 200
        valor %= 200
    elif valor >= 100:
        moedas[0] = valor // 100
        valor %= 100
    elif valor >= 50:
        moedas[1] = valor // 50
        valor %= 50
    elif valor >= 25:
        moedas[2] = valor // 25
        valor %= 25
    elif valor >= 10:
        moedas[3] = valor // 10
        valor %= 10
    elif valor >= 5:
        moedas[4] = valor // 5
        valor %= 5
    elif valor >= 1:
        moedas[5] = valor // 1
        valor %= 1

print("NOTAS:")
print(f"{notas[0]} nota(s) de R$ 100.00")
print(f"{notas[1]} nota(s) de R$ 50.00")
print(f"{notas[2]} nota(s) de R$ 20.00")
print(f"{notas[3]} nota(s) de R$ 10.00")
print(f"{notas[4]} nota(s) de R$ 5.00")
print(f"{notas[5]} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moedas[0]} moeda(s) de R$ 1.00")
print(f"{moedas[1]} moeda(s) de R$ 0.50")
print(f"{moedas[2]} moeda(s) de R$ 0.25")
print(f"{moedas[3]} moeda(s) de R$ 0.10")
print(f"{moedas[4]} moeda(s) de R$ 0.05")
print(f"{moedas[5]} moeda(s) de R$ 0.01")
