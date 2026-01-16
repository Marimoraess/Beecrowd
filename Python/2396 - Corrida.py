n,m=map(int,input().split())
volta=[]
for c in range(n):
    voltas=list(map(int,input().split()))
    soma=sum(voltas)
    volta.append((soma,c+1))
    volta.sort()

print(volta[0][1])
print(volta[1][1])
print(volta[2][1])