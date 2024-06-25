"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
calcule e mostre o comprimento da hipotenusa.
"""
# Biblioteca usada
from math import sqrt
# Variaveis informadas pelo usuário
oposto = float(input("Digite o comprimento do cateto oposto: "))
adjacente = float(input("Digite o comprimento do cateto adjacente: "))
# Sistema para calcular
hipotenusa = sqrt(oposto**2 + adjacente**2)
# Retorno para o usuário
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")