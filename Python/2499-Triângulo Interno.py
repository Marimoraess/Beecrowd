s, n, m = map(int,input().split())
while s != 0 or n != 0 or m != 0:
    c1, c2, c3 = map(int, input().split())
    area = abs(s*(c1/(n+1))*((c3-c2)/(m+1)))
    print(f"{area:.0f}")
    s, n, m = map(int, input().split())