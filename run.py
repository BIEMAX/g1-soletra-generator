import os
from tqdm import tqdm  # Importando o tqdm para a barra de progresso

# Allowed letters and minimum and maximum lengths for the words
# letters = "ATEURMP"
letters = "AUIFTRS"
mandatory_letter = "f"
min_length = 5
max_length = 9

# Load a dictionary of valid Portuguese words
file_path = os.path.join(os.getcwd(), 'utils/words_portuguese_list.txt')
with open(file_path, 'r', encoding='ISO-8859-1') as f:
    portuguese_words = set(f.read().strip().lower().split())

# Dicionários de palavras por número de letras
words_by_length = {i: [] for i in range(min_length, max_length + 1)}

# Filtrar palavras válidas e agrupar por número de letras
for word in tqdm(portuguese_words, desc="Filtrando palavras", unit="palavra"):
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

print(f'Arquivo gerado com {sum(len(words) for words in words_by_length.values())} palavras válidas: {output_file_path}')
