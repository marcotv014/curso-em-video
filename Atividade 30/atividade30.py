"""
Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Impar.
"""
# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
