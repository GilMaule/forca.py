import random

palavras = ['computador', 'python', 'teclado', 'internet', 'programa', 'desenvolver'] # lista com as palavras
secreta = random.choice(palavras).upper() # escolhe uma palavra da lista e converte para maiúsculas

tentativas = 5  # número de tentativas permitidas
letras_descobertas = ['_' for _ in secreta] # substitui as letras da palavra por '_'
letras_digitadas = set() # conjunto para armazenar letras já digitadas

print('\nPalavra Secreta... ')
print(' '.join(letras_descobertas)) # exibe a palavra oculta com '_' separados por espaços

while True:
    letra = input('Digite uma letra...').upper()

    if letra in letras_digitadas:
        print('Letra já foi digitada!')
        continue

    if not letra.isalpha() or len(letra) != 1: # valida se é uma letra válida (não aceita números ou símbolos)
        print('Digite apenas uma letra válida!')
        continue

    letras_digitadas.add(letra) # adiciona a letra ao conjunto de letras digitadas

    if letra in secreta:    # se a letra estiver na palavra secreta
        print('A letra está na palavra')
        for i in range(len(secreta)): # percorre os índices da palavra
            if secreta[i] == letra:   # se a letra do índice for igual à digitada
                letras_descobertas[i] = letra   # substitui o '_' pela letra
    else:
        tentativas -= 1 # reduz o número de tentativas
        print(f'A letra não está na palavra! Tentativas restantes: {tentativas}')
        if tentativas == 0: # se acabar as tentativas
            print('Suas tentativas acabaram')
            print(f'A palavra secreta era: {secreta}')
            break # encerra o jogo

    print('\nPalavra: ')
    print(f'Letras já digitadas: {" ".join(sorted(letras_digitadas))}') # mostra letras já digitadas
    print(' '.join(letras_descobertas)) # mostra o progresso da palavra

    if '_' not in letras_descobertas: # se não houver mais '_', jogador venceu
        print('\nParabéns! Você descobriu a palavra!')
        break