"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.200,00, calcule um aumento de 10%.

Para os inferiores ou iguais o aumento é de 15%.
"""
# Solicita ao usuário que digite o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$"))

# Verifica o aumento baseado no salário
if salario > 1200:
    aumento = salario * 0.10  # 10% de aumento
else:
    aumento = salario * 0.15  # 15% de aumento

# Calcula o novo salário com o aumento
novo_salario = salario + aumento

# Exibe o valor do aumento e o novo salário
print(f"O valor do aumento foi de R${aumento:.2f}")
print(f"O novo salário é de R${novo_salario:.2f}")
