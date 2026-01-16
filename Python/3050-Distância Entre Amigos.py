n = int(input())
predios = list(map(int,input().split()))

dist = 0
k = -1
for i in range(n):
    d = predios[0] + i + predios[i]
    if d > dist:
        dist = d
        k = i
        
max_dist = 0
for j in range(n):
    if j != k:
        max_dist = max(max_dist, predios[k] + abs(k-j) + predios[j])
print(max_dist)