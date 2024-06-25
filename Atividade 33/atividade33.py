"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
# Solicita ao usuário que digite os três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Inicializa as variáveis para armazenar o maior e o menor número
maior = numero1
menor = numero1

# Verifica se o segundo número é maior que o atual maior número
if numero2 > maior:
    maior = numero2

# Verifica se o terceiro número é maior que o atual maior número
if numero3 > maior:
    maior = numero3

# Verifica se o segundo número é menor que o atual menor número
if numero2 < menor:
    menor = numero2

# Verifica se o terceiro número é menor que o atual menor número
if numero3 < menor:
    menor = numero3

# Exibe o maior e o menor número
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
