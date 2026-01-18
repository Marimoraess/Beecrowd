N = int(input())

for c in range(N):
    palavras = input().split()

    palavras.sort(key=len, reverse=True)

    print(" ".join(palavras))