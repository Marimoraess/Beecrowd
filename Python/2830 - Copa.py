K = int(input())
L = int(input())


K -= 1
L -= 1

fase = ["oitavas", "quartas", "semifinal", "final"]

for i in range(4):  # 4 fases

    if K // 2 == L // 2:
        print(fase[i])
        break
    K //= 2
    L //= 2
