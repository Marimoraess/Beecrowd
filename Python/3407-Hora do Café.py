itens, bolinhos_natan = map(int,input().split())
natan = list(map(int,input().split()))
samuel = list(map(int,input().split()))
contnatan = 0
contsamuel = 0
for i in range(itens):
    if natan[i] == 1:
        contnatan += 1
    if samuel[i] == 1:
        contsamuel += 1

if contnatan == bolinhos_natan:
    print('Tudo certo.')
elif contsamuel == bolinhos_natan:
    print('Pegou de Samuel.')
else:
    print('Pegou de um estranho.')