"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""
# Solicita ao usuário que digite a distância da viagem em Km
distancia = float(input("Digite a distância da viagem em Km: "))

# Verifica o preço da passagem com base na distância
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# Exibe o preço da passagem formatado com duas casas decimais
print(f"O preço da passagem é R${preco:.2f}.")
