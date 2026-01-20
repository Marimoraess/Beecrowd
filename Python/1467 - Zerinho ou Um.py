import sys

for linha in sys.stdin:
    A, B, C = map(int, linha.split())
    
    if A == B == C:
        print('*')
    elif A == B:
        print('C')
    elif A == C:
        print('B')
    else:
        print('A')
