"""
Faça um programa que leia o nome completo de uma pessoas, mostrando em seguida o primeiro e o últimonome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
# Solicita ao usuário que digite o nome completo
nome_completo = input("Digite o nome completo da pessoa: ")

# Remove espaços extras no início e no final do nome
nome_completo = nome_completo.strip()

# Divide o nome completo em partes (separa pelos espaços)
partes_do_nome = nome_completo.split()

# O primeiro nome é a primeira parte da lista
primeiro_nome = partes_do_nome[0]

# O último nome é a última parte da lista
ultimo_nome = partes_do_nome[-1]

# Exibe o primeiro e o último nome separadamente
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
