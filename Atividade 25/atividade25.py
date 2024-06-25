"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
"""
# Solicita ao usuário que digite o nome completo
nome_completo = input("Digite o nome completo da pessoa: ")

# Converte o nome para minúsculas para facilitar a comparação
nome_completo = nome_completo.strip().lower()

# Verifica se o nome contém "silva"
if 'silva' in nome_completo:
    print(f"A pessoa tem 'Silva' no nome.")
else:
    print(f"A pessoa não tem 'Silva' no nome.")
