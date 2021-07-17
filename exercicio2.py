# Exercício 2:
#   Faça uma função que receba o nome e sobrenome de uma pessoa e retorne a
#   primeira letra de seu nome e seu sobrenome concatenando com a string
#   @algoritmos.com.br. No algoritmo principal deverá ser apresentada a mensagem
#   ao usuário contendo seu nome completo e seu email.
#   Imprima na tela um teste do seu programa utilizando o seu nome e sobrenome
#   concatenado com os dois últimos dígitos do seu RU.
#   Sra Luciane Kanashiro, seu email é lkanashiro16@algoritmos.com.br

# Function to split characters of a word
def split(word):
    return list(word)

# sample function
def get_last_digits(num, last_digits_count=2):
    return int(str(num)[-last_digits_count:])

# E-mail
email = "@algoritmos.com.br"

# Input names
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
ru = input("Digite seu RU: ")

# Split words
lNome = split(nome)

# RU
ruNum = str(get_last_digits(ru))

# Assembly e-mail
emailGerado = lNome[0]+sobrenome+ruNum+email

# Print Result
print("Sra(o){0} {1}, seu email é: {2}\n".format(nome, sobrenome, emailGerado))