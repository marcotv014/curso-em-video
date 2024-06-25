"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- á vista dinheiro/cheque: 10% de desconto
- á vista no cartão: 5% de desconto
- em até 2x no cartão:
preço normal
- 3x ou mais no cartão: 20% de juros
"""
# Solicita ao usuário que digite o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Exibe as opções de pagamento
print("\nCondições de pagamento:")
print("[1] À vista dinheiro/cheque: 10% de desconto")
print("[2] À vista no cartão: 5% de desconto")
print("[3] Em até 2x no cartão: preço normal")
print("[4] 3x ou mais no cartão: 20% de juros")

# Solicita ao usuário que escolha a condição de pagamento
opcao = int(input("\nEscolha a condição de pagamento (1/2/3/4): "))

# Calcula o valor final com base na condição de pagamento
if opcao == 1:
    valor_final = preco * 0.90
    condicao = "À vista dinheiro/cheque"
elif opcao == 2:
    valor_final = preco * 0.95
    condicao = "À vista no cartão"
elif opcao == 3:
    valor_final = preco
    condicao = "Em até 2x no cartão"
elif opcao == 4:
    valor_final = preco * 1.20
    condicao = "3x ou mais no cartão"
else:
    valor_final = None
    condicao = "Opção inválida"

# Exibe o valor final a ser pago
if valor_final is not None:
    print(f"\nCondição de pagamento: {condicao}")
    print(f"Valor final a ser pago: R$ {valor_final:.2f}")
else:
    print("\nOpção de pagamento inválida. Por favor, escolha uma opção válida.")
