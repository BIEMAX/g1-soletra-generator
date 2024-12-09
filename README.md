# G1 Soletra Generator

Esse projeto tem como o intuito de pesquisa apenas, não tem como intuito comercialização ou trapacear.

O intuito é encontrar palavras do jogo [G1 Soletra](https://g1.globo.com/jogos/soletra/) que consiste em encontrar palavras considerando uma combinação de letras e que contenha a letra mandatório (geralmente no centro da tela na cor verde).

# Requisitos

1. Python3
2. Dicionário em português das palavras dentro do diretório raiz, com o nome `portuguese_dictionary.txt`.
> **Nota:** Você pode atualizar o seu dicionário como bem entender, desde que não mude o atual formato.

# Como rodar

1. Instale o Python 3
2. Rode o comando abaixo para instalar as dependências:
```bash
pip install -r requirements.txt
```
3. Rode o comando abaixo para executar o código:
```bash
python run.py
```
4. Ao rodar o programa, será necessário responder as perguntas abaixo:
```bash
Digite as letras do dia no jogo (todas as 7 letras): 
aveotil # exemplo de letras

Digite a letra obrigatória para as palavras: 
f       # letra obrigatória do jogo que deve conter em todas as palavras

Digite o tamanho mínimo das palavras: 
4       # tamanho mínimo das palavras (quantidade de caracteres)

Digite o tamanho máximo das palavras: 
10      # tamanho máximo das palavras (quantidade de caracteres)
```
5. Será exportado o arquivo `valid_words.txt` na pasta raiz do projeto.
6. ENJOY :D 