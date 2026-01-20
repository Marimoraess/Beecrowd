caso = 1

while True:
    entrada = input().split()
    N, M = map(int, entrada)
    if N == 0 and M == 0:
        break

    temperaturas = [int(input()) for _ in range(N)]

    soma = sum(temperaturas[:M])
    min_media = int(soma / M)
    max_media = int(soma / M)

    for i in range(1, N - M + 1):
        soma = soma - temperaturas[i - 1] + temperaturas[i + M - 1]
        media = int(soma / M)
        if media < min_media:
            min_media = media
        if media > max_media:
            max_media = media

    print(f"Teste {caso}")
    print(f"{min_media} {max_media}\n")
    caso += 1
