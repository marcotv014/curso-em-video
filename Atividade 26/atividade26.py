"""
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A":

Em que posição ela aparece a primeira vez:

Em que posição ela aparece a última vez.
"""
# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Converte a frase para minúsculas para facilitar a contagem e busca
frase_minuscula = frase.lower()

# Conta quantas vezes a letra 'a' aparece na frase
quantidade_a = frase_minuscula.count('a')

# Encontra a posição da primeira ocorrência da letra 'a'
primeira_posicao = frase_minuscula.find('a')

# Encontra a posição da última ocorrência da letra 'a'
ultima_posicao = frase_minuscula.rfind('a')

# Exibe os resultados
print(f"A letra 'A' aparece {quantidade_a} vezes na frase.")
if quantidade_a > 0:
    print(f"A primeira vez que 'A' aparece é na posição: {primeira_posicao + 1}")  # +1 para mostrar posição humana (começando de 1)
    print(f"A última vez que 'A' aparece é na posição: {ultima_posicao + 1}")      # +1 para mostrar posição humana (começando de 1)
else:
    print("A letra 'A' não aparece na frase.")
