"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
"""
# Biblioteca utilizada
from math import sin, cos, tan, radians
# Variavel informada pelo usuário
angulo_graus = float(input("Digite um ângulo em graus: "))
# Sistema de calculo
angulo_radiante = radians(angulo_graus)
seno = sin(angulo_radiante)
cosseno = cos(angulo_radiante)
tangente = tan(angulo_radiante)
# Imprimir o resultado para o usuário
print(f"""
O ângulo de {angulo_graus} graus tem: 
Seno: {seno:.4f}
Cosseno: {cosseno:.4f}
Tangente: {tangente:.4f}
""")