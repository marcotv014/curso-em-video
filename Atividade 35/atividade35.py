"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
# Solicita ao usuário que digite o comprimento das três retas
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

# Verifica a condição de existência de triângulo
if a < b + c and b < a + c and c < a + b:
    print("Com essas medidas é possível formar um triângulo.")
else:
    print("Com essas medidas não é possível formar um triângulo.")
