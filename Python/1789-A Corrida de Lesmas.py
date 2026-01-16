while True:
    try:
        lesmas = int(input())
        velocidades = list(map(int,input().split()))
        if max(velocidades) < 10:
            print('1')
        elif 10 <= max(velocidades) < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break