

def main():
    try:
        T = int(input())
    except:
        return

    for _ in range(T):
        M_N = input().split()
        while len(M_N) < 2:
            M_N = input().split()

        M = int(M_N[0])
        N = int(M_N[1])

        dicio = {}

      
        for __ in range(M):
            jap = input().rstrip('\n')
            port = input().rstrip('\n')
            dicio[jap] = port

       
        for __ in range(N):
            linha = input().rstrip('\n')

            if linha == "":
                print("")
                continue

            palavras = linha.split()
            traduzidas = []

            for p in palavras:
                if p in dicio:
                    traduzidas.append(dicio[p])
                else:
                    traduzidas.append(p)

            print(" ".join(traduzidas))

        print()  

main()
