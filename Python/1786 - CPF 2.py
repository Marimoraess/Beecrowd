import sys

for linha in sys.stdin:
    linha = linha.strip()
    if len(linha) != 9:
        continue  
    numeros = [int(d) for d in linha]

    soma_b1 = sum((i + 1) * numeros[i] for i in range(9))
    b1 = soma_b1 % 11
    if b1 == 10:
        b1 = 0

    soma_b2 = sum((9 - i) * numeros[i] for i in range(9))
    b2 = soma_b2 % 11
    if b2 == 10:
        b2 = 0

    cpf_formatado = (
        f"{linha[0:3]}.{linha[3:6]}.{linha[6:9]}-{b1}{b2}"
    )
    print(cpf_formatado)
