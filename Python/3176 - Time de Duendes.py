N = int(input())
duendes = []

for _ in range(N):
    dados = input().split()
    nome = dados[0]
    idade = int(dados[1])
    duendes.append((nome, idade))

duendes.sort(key=lambda x: (-x[1], x[0]))

t = N // 3 
lideres = duendes[:t]
entregadores = duendes[t:2*t]
pilotos = duendes[2*t:3*t]

for i in range(t):
    print(f"Time {i+1}")
    print(f"{lideres[i][0]} {lideres[i][1]}")
    print(f"{entregadores[i][0]} {entregadores[i][1]}")
    print(f"{pilotos[i][0]} {pilotos[i][1]}\n")
