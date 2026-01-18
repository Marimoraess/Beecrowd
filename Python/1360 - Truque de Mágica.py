# Mapas de ordem
suit_order = {'H': 0, 'C': 1, 'D': 2, 'S': 3}
value_order = ['1','2','3','4','5','6','7','8','9','T','J','Q','K']
value_index = {v: i for i, v in enumerate(value_order)}

def next_value(v, k):
    return value_order[(value_index[v] + k) % 13]

def card_key(card):
    return (suit_order[card[1]], value_index[card[0]])

order_to_number = {
    (0,1,2): 1,
    (0,2,1): 2,
    (1,0,2): 3,
    (1,2,0): 4,
    (2,0,1): 5,
    (2,1,0): 6
}

n = int(input())
for _ in range(n):
    cards = input().split()
    
    y = cards[0]
    rest = cards[1:]
    
    sorted_rest = sorted(rest, key=card_key)
    perm = tuple(sorted_rest.index(c) for c in rest)
    
    number = order_to_number[perm]
    hidden_value = next_value(y[0], number)
    
    print(hidden_value + y[1])
