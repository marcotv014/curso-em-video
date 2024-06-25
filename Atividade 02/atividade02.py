"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
nome = input("Digite seu nome: ") # input = Quando você precisa receber uma informação variavel do usuário.
print(f"É um prazer te conhecer, {nome}!") # Dessa forma é um metodo mais moderno de se formatar o retorno para o usuário mas temos também:
# print("É um prazer te conhecer, {}!".format(nome)) # Dessa forma foi como foi mostrado no curso.