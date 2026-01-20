n = int(input())  
lista = [] 
count = 0  

for c in range(n):
    m = int(input())  
    p = list(map(int, input().split()))  
    lista.append(p)  
for lista2 in lista:
    lista_original = lista2[:]  
   
    for i in range(len(lista2)):
        for j in range(len(lista2) - 1 - i):
            if lista2[j] < lista2[j + 1]:
                lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]
    
   
    count = 0
    for i in range(len(lista2)):
        if lista2[i] == lista_original[i]: 
            count += 1
    

    print(count)
