"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
# Biblioteca utilizada
from random import shuffle
# Variaveis informadas pelo usuario
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
# Sistema criado
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
# retorno para o usuário
print(f"A ordem de apresentação dos trabalhos será: ")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}. {aluno}")