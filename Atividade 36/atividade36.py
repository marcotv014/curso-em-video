"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salario então o empréstimo será negado.
"""
# Solicita ao usuário que digite o valor da casa, o salário do comprador e em quantos anos vai pagar
valor_casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o salário do comprador: R$"))
anos = int(input("Digite em quantos anos pretende pagar o empréstimo: "))

# Calcula o valor da prestação mensal
meses = anos * 12
prestacao_mensal = valor_casa / meses

# Verifica se a prestação mensal não excede 30% do salário
porcentagem_salario = salario * 0.30

# Exibe o resultado da análise de crédito
if prestacao_mensal <= porcentagem_salario:
    print(f"Empréstimo aprovado! O valor da prestação mensal será de R${prestacao_mensal:.2f}.")
else:
    print(f"Empréstimo negado! O valor da prestação mensal de R${prestacao_mensal:.2f} excede 30% do seu salário.")
