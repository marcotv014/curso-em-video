"""
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:

- O primeiro valor é maior

- O segundo valor é menor

- Não exoste valor maior, os dois são iguais
"""
# Informação dos numeros
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro numero número: "))
# Sistema de comparação dos valores
if n1 > n2:
    print(f"O primeiro valor que é {n1} é maior que o segundo valor que é {n2}")
elif n2 > n1:
    print(f"O primeiro valor que é {n2} é maior que o segundo valor que é {n1}")
elif n1 == n2:
    print(f"Os valores que foram passados não iguais")
else:
    print(f"Confira os valores algo esta errado!")