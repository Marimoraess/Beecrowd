
def main():
    while True:
        try:
            linha = input()
        except:
            break

        partes = ['']
        atual = 0

        for c in linha:
            if c == '[':
                partes.insert(0, '')
                atual = 0
            elif c == ']':
                partes.append('')
                atual = len(partes) - 1
            else:
                partes[atual] += c

        print("".join(partes))

main()
