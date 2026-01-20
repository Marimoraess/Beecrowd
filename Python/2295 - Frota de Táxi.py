A, G, Ra, Rg = map(float, input().split())

custo_alcool = A / Ra
custo_gasolina = G / Rg

if custo_alcool < custo_gasolina:
    print("A")
else:
    print("G")
