inscritos_yes = []
inscritos_no = []

nomes_processados_yes = set()

vencedor_nome = ""
vencedor_tam = -1

while True:
    entrada = input()
    
    if entrada == "FIM":
        break
        
    dados = entrada.split()
    nome = dados[0]
    opcao = dados[1]
    
    if opcao == "YES":
        if nome not in nomes_processados_yes:
            inscritos_yes.append(nome)
            nomes_processados_yes.add(nome)
        
        
        if len(nome) > vencedor_tam:
            vencedor_nome = nome
            vencedor_tam = len(nome)
            
    else:
        
        inscritos_no.append(nome)

inscritos_yes.sort()
inscritos_no.sort()

for nome in inscritos_yes:
    print(nome)
    

for nome in inscritos_no:
    print(nome)
    

print()


print("Amigo do Habay:")
print(vencedor_nome)
