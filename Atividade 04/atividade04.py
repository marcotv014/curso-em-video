"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
"""
tipo = input("Digite algo: ") # objeto
print(f"O tipo primitivo desse valor é: {type(tipo)}") # aqui ele me da o retorno do tipo primitivo do input
print(f"Só tem espaços? {tipo.isspace()}") # aqui vejo se so tem espaços no input
print(f"É um número? {tipo.isnumeric()}") # aqui vejo se é um numero no input
print(f"É alfabético? {tipo.isalpha()}") # aqui vejo se é letra o input
print(f"É alfanumérico? {tipo.isalnum()}") # aqui vejo se ele é alfanumérico
print(f"Está em maiúsculo? {tipo.isupper()}") # aqui vejo se esta em maiusculo
print(f"Está em minusculo? {tipo.islower()}") # aqui vejo se esta em minusculo
print(f"Está capitalizada? {tipo.istitle()}") # aqui vejo se esta capitalizada
