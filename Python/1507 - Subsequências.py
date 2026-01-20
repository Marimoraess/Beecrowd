N = int(input())

for _ in range(N):
    S = input()
    Q = int(input())

    pos = [[] for __ in range(52)]

   
    for i in range(len(S)):
        c = S[i]
        if 'a' <= c <= 'z':
            idx = ord(c) - 97
        else:
            idx = ord(c) - 65 + 26
        pos[idx].append(i)

    for __ in range(Q):
        R = input()
        last = -1
        ok = True

        for c in R:
            if 'a' <= c <= 'z':
                idx = ord(c) - 97
            else:
                idx = ord(c) - 65 + 26

            L = pos[idx]
            if not L:
                ok = False
                break

            lo = 0
            hi = len(L) - 1
            ans = -1
            seek = last + 1

            while lo <= hi:
                mid = (lo + hi) // 2
                if L[mid] >= seek:
                    ans = L[mid]
                    hi = mid - 1
                else:
                    lo = mid + 1

            if ans == -1:
                ok = False
                break

            last = ans

        if ok:
            print("Yes")
        else:
            print("No")
