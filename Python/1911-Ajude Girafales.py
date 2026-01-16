alunos = int(input())
while alunos != 0:
    dicionario = {}
    lista = []
    falsas = 0
    for i in range(alunos):
        dicionario['nome'], dicionario['original'] = input().split()
        lista.append(dicionario.copy())

    dicionario_aux = {}
    presentes = int(input())
    for i in range(presentes):
        dicionario_aux['nome'], dicionario_aux['aula'] = input().split()
        for j in range(alunos):
            if dicionario_aux['nome'] == lista[j]['nome']:
                if dicionario_aux['aula'] != lista[j]['original']:
                    diferencas = 0
                    for k in range(len(dicionario_aux['aula'])):
                        if dicionario_aux['aula'][k] != lista[j]['original'][k]:
                            diferencas += 1
                    if diferencas > 1:
                        falsas += 1
                break
    print(falsas)
    alunos = int(input())