"""
Escreva um programa que converta um temperatura digitado em ºC e converta para ºF.
"""
# Pegar informação do usuário
cel = float(input("Digite a temperatura em ºC: "))
# Irei fazer o sistem que ira fazer a conversão 
fah = (cel * 9 / 5) + 32
# irei retornar para o usuário
print(f"A temperatura de {cel:.2f}ºC é equivalente a {fah:.2f}ºF")