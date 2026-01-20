cod, quant = map(int, input().split())

if cod == 1:
    total = 4.0 * quant
elif cod == 2:
    total = 4.5 * quant
elif cod == 3:
    total = 5.0 * quant
elif cod == 4:
    total = 2.0 * quant
elif cod == 5:
    total = 1.5 * quant

print(f'Total: R$ {total:.2f}')
