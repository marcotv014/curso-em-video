"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar , 
sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
"""
# aqui pego as informações variaveis do usuário
km = float(input("Digite a quantidade de Km percorrido: "))
dias = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
# custos definidos
cdias = 60.00
ckm = 0.15
# Sistema de calculo 
total = (dias * cdias) + (km * ckm)
# Retorno para o usuário
print(f"O total a pagar é: R${total:.2f}")