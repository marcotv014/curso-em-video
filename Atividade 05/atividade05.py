"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
# Aqui pego a informação do usuario o numero.
n1 = int(input("Digite um número: "))
# Agora faço que o sistema calcule o exercicio solicitado.
su = n1 + 1 # aqui pego o numero e sumo mais um para saber o sucessor do numero que o usuário me passou.
an = n1 - 1 # aqui faço alcontrario do que fiz antes para saber o antecessor do número.
# Agora retorno para o usuário as informações.
print(f"O número digitado foi: {n1}")
print(f"O sucessor desse número é: {su}")
print(f"O antecessor desse número é: {an}")