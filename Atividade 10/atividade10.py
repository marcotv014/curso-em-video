"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

Considere
US$1,00 = R$3,27
"""
# irei passar uma informação pro usuario
print("Ola, seja bem vindo!, Aqui ira saber quantos Dólares ira conseguir comprar!")
print()
# irei pegar a informação do usuario
n = float(input("Quanto você tem agora: "))
# agora irei fazer o sistema para saber quantos o usuario ira conseguir comprar
tx = 3.27
d = n / tx
# retornando para o usuraio
print(f"Com R${n:.2f}, você pode comprar US${d:.2f}")