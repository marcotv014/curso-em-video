"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.

- Se é a hora de se alistar.

- Se já passou do tempo de alistamento.

Seu programa também devera mostrar o tempo que falta ou que passou do prazo.
"""
# Bibliotecas utilizadas
from datetime import datetime
# Informações variaveis
ano_de_nacimento = int(input("Digite o ano de seu nacimento: "))
# Informação do ano atual
ano_atual = datetime.now().year
# sistema para ver a idade do usuário naquele ano
idade = (ano_atual - ano_de_nacimento)
# sistema para saber que apos 18 anos ele ja esta apto para se alistar
ano_alistamento = (ano_de_nacimento + 18)
# Verifica o status de alistamento e exibe a mensagem apropriada
if idade < 18:
    anos_faltantes = 18 - idade
    print(f"Você ainda vai se alistar ao serviço militar. Faltam {anos_faltantes} anos.")
    print(f"Seu alistamento será em {ano_alistamento}.")
elif idade == 18:
    print("É hora de se alistar ao serviço militar.")
else:
    anos_passados = idade - 18
    print(f"Já passou do tempo de alistamento. Você deveria ter se alistado há {anos_passados} anos.")
    print(f"Seu alistamento foi em {ano_alistamento}.")