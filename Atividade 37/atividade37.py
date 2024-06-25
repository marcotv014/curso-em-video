"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversção:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
# aqui irei pedir o numero inteiro para o usuário
n = int(input("Digite um número inteiro: "))
# informação para o usuario para converter
print("""
Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
""")
# Pegar a escolha dele
escolha = int(input("Sua escolha: "))
# Sistema para conversão
if escolha == 1:
    resultado = bin(n)[2:]
    base = "BINÁRIO"
elif escolha == 2:
    resultado = oct(n)[2:]  # octal, remove os dois primeiros caracteres '0o'
    base = "OCTAL"
elif escolha == 3:
    resultado = hex(n)[2:]  # hexadecimal, remove os dois primeiros caracteres '0x'
    base = "HEXADECIMAL"
else:
    resultado = None
    base = None
    # Exibe o resultado da conversão
if resultado is not None:
    print(f"O número {n} convertido para {base} é igual a {resultado}.")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")