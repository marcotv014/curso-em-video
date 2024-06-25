"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas:

O nome com todas as letras minusculas:

Quantas letras ao todo (sem considerar os espaços):

Quantoas letras tem o primeiro nome:
"""
# Solicita ao usuário que insira o nome completo
nome_completo = input("Digite seu nome completo: ")

# Exibe o nome com todas as letras maiúsculas
nome_maiusculas = nome_completo.upper()
print(f"Nome com todas as letras maiúsculas: {nome_maiusculas}")

# Exibe o nome com todas as letras minúsculas
nome_minusculas = nome_completo.lower()
print(f"Nome com todas as letras minúsculas: {nome_minusculas}")

# Calcula a quantidade de letras no nome completo (sem considerar os espaços)
quantidade_letras = len(nome_completo.replace(" ", ""))
print(f"Quantidade de letras (sem considerar os espaços): {quantidade_letras}")

# Calcula a quantidade de letras no primeiro nome
primeiro_nome = nome_completo.split()[0]
quantidade_letras_primeiro_nome = len(primeiro_nome)
print(f"Quantidade de letras no primeiro nome: {quantidade_letras_primeiro_nome}")
