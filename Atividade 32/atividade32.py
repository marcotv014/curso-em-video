"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
# Solicita ao usuário que digite um ano
ano = int(input("Digite um ano para verificar se é bissexto: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
