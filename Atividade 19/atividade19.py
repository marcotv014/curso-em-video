"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
# Bibliotecas usadas
from random import choice
# informações variaveis
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
# Sistema que sorteia 
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)
# Retorno para o usuário
print(f"""
O aluno escolhido para apagar o quadro é: {escolhido}
""")