v = int(input())
p = int(input())
if 2 <= p <= 18:
    parcelas = v//p
    resto = v % p
    for i in range(p):
        if resto != 0:
            print(f"{parcelas + 1}")
            resto -= 1
        else:
            print(f"{parcelas}")