# Buffer para armazenar os números lidos
tokens = []

while True:
    # --- Bloco de Leitura ---
    # Garante que temos pelo menos 3 números (N, k, m)
    try:
        while len(tokens) < 3:
            linha = input()
            if linha.strip(): # Se a linha não for vazia
                tokens.extend(linha.split())
    except EOFError:
        break # Para se o input acabar

    # Pega N, k, m
    N = int(tokens.pop(0))
    k = int(tokens.pop(0))
    m = int(tokens.pop(0))

    # Condição de parada (0 0 0)
    if N == 0 and k == 0 and m == 0:
        break

    # --- Bloco de Lógica ---
    
    # Cria a roda de pessoas (1 a N). 0 significa "saiu".
    pessoas = list(range(1, N + 1))
    restantes = N

    # Ponteiros (índices 0 a N-1)
    # idx1 (Horário): começa "antes" do 0 (ou seja, N-1)
    # idx2 (Anti-horário): começa "depois" do último (ou seja, 0)
    idx1 = N - 1
    idx2 = 0

    resultado = []

    while restantes > 0:
        # Movimento Horário (k passos)
        passos = k
        while passos > 0:
            idx1 = (idx1 + 1) % N
            if pessoas[idx1] != 0: # Se a pessoa ainda está lá
                passos -= 1
        
        # Movimento Anti-Horário (m passos)
        passos = m
        while passos > 0:
            idx2 = (idx2 - 1 + N) % N
            if pessoas[idx2] != 0: # Se a pessoa ainda está lá
                passos -= 1
        
        # Pega os valores
        p1 = pessoas[idx1]
        p2 = pessoas[idx2]

        # Formata o primeiro número (3 espaços à direita)
        texto_par = "{:>3}".format(p1)
        
        # Remove p1
        pessoas[idx1] = 0
        restantes -= 1

        # Se p2 for diferente de p1, adiciona e remove p2
        if p1 != p2:
            texto_par += "{:>3}".format(p2)
            pessoas[idx2] = 0
            restantes -= 1
        
        resultado.append(texto_par)

    # Imprime a linha final com vírgulas
    print(",".join(resultado))