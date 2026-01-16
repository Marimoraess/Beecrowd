id1 = input()
id2 = input()
id3 = input()
if id1 == 'vertebrado':
    if id2 == 'ave':
        if id3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if id3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if id2 == 'inseto':
        if id3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if id3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')