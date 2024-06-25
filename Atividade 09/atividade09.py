"""
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
"""
"""
# Irei fazer de dois modos essa atividade
# Modo com mais linhas de codigo
# Aqui pego a informação do usuário
n = int(input("Digite o número da tabuada que deseja: "))
# aqui irei fazer o sistema para fazer a tabuado do usuario
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
# Agora irei retorna para o usuário
print(f'''
A tabuado do {n} é:
{n} x 1 = {n1}
{n} x 2 = {n2}
{n} x 3 = {n3}
{n} x 4 = {n4}
{n} x 5 = {n5}
{n} x 6 = {n6}
{n} x 7 = {n7}
{n} x 8 = {n8}
{n} x 9 = {n9}
{n} x 10 = {n10}
    ''')
# dessa forma é de um jeito mais trabalhoso para fazer
"""
# irei fazer de um jeito bem diferente agora
while True:
    # Solicita ao usuário um número
    numero = int(input("Digite um número para ver sua tabuada (ou 0 para sair): "))

    # Verifica se o usuário deseja sair
    if numero == 0:
        print("Encerrando o programa.")
        break

    # Imprime a tabuada do número fornecido
    print(f"\nTabuada de {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

    print("\n")  # Adiciona uma linha em branco para separar as tabuadas
