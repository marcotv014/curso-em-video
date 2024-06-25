"""
Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessário para pintá-la, 
sabendo que cada litro de tinta, pinta uma área de 2m².
"""
# Irei colocar um aviso antes de qualquer coisa
print("Seja bem vindo!, Aqui um sistema de calculo de gasto para pintores")
# Pegar informações
lar = float(input("Digite a Largura da parede: "))
alt = float(input("Digite a Altura da parede: "))
lit = float(input("Quantos litros de tinta você gasta para pintar 2m²: "))
# Informações para calcular
ar = lar * alt
q = ar / lit
# retorno para o usuário
print(f"""
A área da parede é de {ar:.2f}m².
Você precisa de {q:.2f} litros de tinta de para pintar a parede.
""")