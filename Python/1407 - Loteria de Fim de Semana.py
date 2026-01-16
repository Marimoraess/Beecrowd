while True:
    line = input().strip()
    if not line:
        continue

    N, C, K = map(int, line.split())
    if N == 0 and C == 0 and K == 0:
        break

    # contador de frequências (1..K)
    freq = [0] * (K + 1)

    for _ in range(N):
        nums = list(map(int, input().split()))
        for x in nums:
            freq[x] += 1

    # encontrar menor frequência entre 1..K
    menor = freq[1]
    i = 2
    while i <= K:
        if freq[i] < menor:
            menor = freq[i]
        i += 1

    # imprimir todos que têm essa menor frequência
    primeira = True
    j = 1
    while j <= K:
        if freq[j] == menor:
            if primeira:
                print(j, end="")
                primeira = False
            else:
                print(" " + str(j), end="")
        j += 1
    print()
