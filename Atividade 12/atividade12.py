"""
Faça um algoritmo que leia a preço um produto e mostre seu novo preço, com 5% de desconto.
"""
# Retirar unformação do usuario
pre = float(input("Digite o valor para aplicar o desconto: "))
# Formula pra aplicar o desconto
des = pre * 0.05
nov = pre - des
# retorno para o usuario
print(f"""
O preço original do produto é: R${pre:.2f}
O desconto  de 5% é: R${des:.2f}
O novo preço do produto com desconto é: R${nov:.2f}
""")