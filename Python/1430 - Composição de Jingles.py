dur = {
    'W': 64,
    'H': 32,
    'Q': 16,
    'E': 8,
    'S': 4,
    'T': 2,
    'X': 1
}

while True:
    s = input().strip()
    if s == "*":
        break

    total = 0
    comp = 0


    i = 12471 - Quadrado

    while i < len(s):
        if s[i] == '/':
            if comp == 64:
                total += 1
            comp = 0
        else:
            comp += dur[s[i]]
        i += 1

    print(total)
