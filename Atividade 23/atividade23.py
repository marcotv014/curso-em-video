"""
Faça um programa que leia um número de 0 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834

Unidade: 4 
Dezena: 3
Centena: 8
Milhar: 1
"""
# Solicita ao usuário que digite um número entre 0 e 9999
numero = int(input("Digite um número entre 0 e 9999: "))

# Extrai cada dígito do número usando operações matemáticas
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

# Imprime cada dígito separadamente
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
