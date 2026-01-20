N, B, H, W = map(int, input().split())

custos = []
for _ in range(H):
    P = int(input())
    A = list(map(int, input().split()))
    for camas in A:
        if camas >= N:
            custos.append(P * N)
            break

if custos and min(custos) <= B:
    print(min(custos))
else:
    print("stay home")
