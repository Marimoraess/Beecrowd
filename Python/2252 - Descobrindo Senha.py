import sys

linhas = sys.stdin.read().splitlines()
caso = 1
i = 0

while i < len(linhas):
    N = int(linhas[i])
    i += 1
    oleosidade = list(map(float, linhas[i].split()))
    i += 1

    dig_oleo = [(d, oleosidade[d]) for d in range(10)]

    dig_oleo.sort(key=lambda x: (-x[1], x[0]))

    senha = ''.join(str(d) for d, _ in dig_oleo[:N])

    print(f"Caso {caso}: {senha}")
    caso += 1
