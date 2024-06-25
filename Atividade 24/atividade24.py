"""
Crie um programa que leia o nome de uma cidade e diga se ela comelça ou não com o nome "Santo".
"""
# Solicita ao usuário que digite o nome da cidade
cidade = input("Digite o nome da cidade: ")

# Converte o nome da cidade para minúsculas para facilitar a comparação
cidade = cidade.strip().lower()

# Verifica se o nome da cidade começa com "santo"
if cidade[:5] == "santo":
    print(f"A cidade {cidade.capitalize()} começa com 'Santo'.")
else:
    print(f"A cidade {cidade.capitalize()} não começa com 'Santo'.")
