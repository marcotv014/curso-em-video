"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salárop, 
com 15% de aumento.
"""
# Solicita ao usuário o salário atual do funcionário
salario_atual = float(input("Digite o salário atual do funcionário: R$ "))

# Calcula o aumento de 15%
aumento = salario_atual * 0.15

# Calcula o novo salário com o aumento
novo_salario = salario_atual + aumento

# Imprime o resultado
print(f"O salário atual do funcionário é: R$ {salario_atual:.2f}")
print(f"O aumento de 15% é: R$ {aumento:.2f}")
print(f"O novo salário do funcionário com aumento é: R$ {novo_salario:.2f}")