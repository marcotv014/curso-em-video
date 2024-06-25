"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
de acordo com a idade:

-Aaté 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
"""
from datetime import datetime

# Solicita ao usuário que digite o ano de nascimento do atleta
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

# Obtém o ano atual
ano_atual = datetime.now().year

# Calcula a idade do atleta
idade = ano_atual - ano_nascimento

# Determina a categoria do atleta e exibe a mensagem apropriada
if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Junior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"

# Exibe a categoria do atleta
print(f"O atleta tem {idade} anos e está na categoria {categoria}.")
