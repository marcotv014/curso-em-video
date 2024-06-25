"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir 
qual foi o número escolhido pelo computador.

Oprograma deverá escrever na tela se o usuário venceu ou perdeu
"""
import random

# Computador escolhe um número aleatório entre 0 e 5
numero_aleatorio = random.randint(0, 5)

# Solicita ao usuário que tente adivinhar o número
tentativa = int(input("Tente adivinhar o número que o computador pensou (entre 0 e 5): "))

# Verifica se o número escolhido pelo usuário é igual ao número pensado pelo computador
if tentativa == numero_aleatorio:
    print(f"Parabéns! Você acertou. O número pensado pelo computador era {numero_aleatorio}.")
else:
    print(f"Você errou. O número pensado pelo computador era {numero_aleatorio}.")
