import os
from tqdm import tqdm  # Importando o tqdm para a barra de progresso

# Allowed letters and minimum and maximum lengths for the words
letters = ""
mandatory_letter = ""
min_length = 0
max_length = 0

def pergunta_letras():
    global letters
    while True:
        resposta = input("Digite as letras do dia no jogo (todas as 7 letras): \n")
        if resposta.isalpha() and resposta.__len__() == 7:
            letters = resposta
            break
        else:
            print("\nResposta inválida! Por favor, digite apenas letras e no máximo 7 letras")

def pergunta_letra_obrigatoria():
    global mandatory_letter
    while True:
        resposta = input("\nDigite a letra obrigatória para as palavras: \n")
        if resposta.isalpha() and resposta.__len__() == 1:
            mandatory_letter = resposta
            break
        else:
            print("\nResposta inválida! Por favor, digite apenas uma letra")

def pergunta_tamanho_min():
    global min_length
    while True:
        resposta = input("\nDigite o tamanho mínimo das palavras: \n")
        if resposta.isnumeric():
            min_length = int(resposta)
            break
        else:
            print("\nResposta inválida! Por favor, digite apenas números\n")

def pergunta_tamanho_max():
    global max_length
    while True:
        resposta = input("\nDigite o tamanho máximo das palavras: \n")
        if resposta.isnumeric():
            max_length = int(resposta)
            break
        else:
            print("\nResposta inválida! Por favor, digite apenas números\n")

def gera_dicionario_palavras():
    # Load a dictionary of valid Portuguese words
    file_path = os.path.join(os.getcwd(), './portuguese_dictionary.txt')
    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        portuguese_words = set(f.read().strip().lower().split())

    # Dicionários de palavras por número de letras
    words_by_length = {i: [] for i in range(min_length, max_length + 1)}

    # Filtrar palavras válidas e agrupar por número de letras
    for word in tqdm(portuguese_words, desc="\nFiltrando palavras", unit="palavra"):
        if min_length <= len(word) <= max_length and mandatory_letter in word and all(c in letters.lower() for c in word):
            words_by_length[len(word)].append(word)

    # Ordenar cada lista por ordem alfabética
    for length in words_by_length:
        words_by_length[length] = sorted(words_by_length[length])

    # Path to output file
    output_file_path = os.path.join(os.getcwd(), 'valid_words.txt')

    # Write the valid words to a text file with progress bar
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Exportar as palavras por número de letras, começando de 4 até 11
        for length in range(min_length, max_length + 1):
            for word in words_by_length[length]:
                output_file.write(word + '\n')  # Escrever cada palavra em uma nova linha

    print(f'\nArquivo gerado com {sum(len(words) for words in words_by_length.values())} palavras válidas: {output_file_path}\n')

pergunta_letras()
pergunta_letra_obrigatoria()
pergunta_tamanho_min()
pergunta_tamanho_max()
gera_dicionario_palavras()