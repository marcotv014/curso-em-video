"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

Ex:
Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.
"""
# Biblioteca utulizada 
from math import trunc
# Receber informação variavel do usuário
n = float(input("Digite um número real: "))
# Sistema para informa o numero inteiro
int = trunc(n)
# retorno para o usuário
print(f"O número {n:.2f} tem a parte inteira {int:.2f}")