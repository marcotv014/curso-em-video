"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
"""
# Solicita ao usuário que digite a velocidade do carro
velocidade = float(input("Digite a velocidade do carro (em Km/h): "))

# Verifica se a velocidade ultrapassa o limite de 80 Km/h
limite = 80
if velocidade > limite:
    # Calcula a quantidade de Km acima do limite
    km_acima = velocidade - limite
    
    # Calcula o valor da multa (R$7,00 por cada Km acima do limite)
    valor_multa = km_acima * 7
    
    # Exibe a mensagem de que o carro foi multado e o valor da multa
    print(f"Você ultrapassou o limite de velocidade. Você foi multado em R${valor_multa:.2f}.")
else:
    print("Velocidade dentro do limite. Continue dirigindo com segurança.")
