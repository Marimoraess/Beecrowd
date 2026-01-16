
N_str = input()
if not N_str:
    pass
else:
    N = int(N_str)
    
    
    initial_str = input().split()
    initial = [int(x) for x in initial_str]
   
    target_str = input().split()
    target = [int(x) for x in target_str]

    map_perm = [0] * (N + 1)
    i = 0
    while i < N:
        map_perm[initial[i]] = target[i]
        i += 1
        
    sigma = [0] * N
    i = 0
    while i < N:
        sigma[i] = map_perm[i + 1]
        i += 1

    bit = [0] * (N + 1)
    total_inversions = 0
    
    index = 0
    
    while index < N:
        value = sigma[index]
        s = 0
        k = value
        while k > 0:
            s += bit[k]
            
            k -= k & (-k)
        
        count_smaller_or_equal = s
        
        inversions_at_index = index - count_smaller_or_equal
        total_inversions += inversions_at_index
        
        k = value
        while k <= N:
            bit[k] += 1
            
            k += k & (-k)

        index += 1

        print("Possible")
    else:
        print("Impossible")