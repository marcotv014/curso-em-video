"""
Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada.
"""
# Aqui irei pedir um número para o usuário
n1 = int(input("Digite um número: "))
# Aqui irei desenvolver os caulos para o sistema realizar apos pegar o número.
d = n1 * 2 # Aqui é multiplicação para saber o sobro do valor.
t = n1 * 3 # Aqui é para saber o tripli do valor.
rq = n1*(n1/100)
# aqui irei retornar as informações para o usuário.
print(f"O número digitado foi: {n1}")
print(f"O dobro do número é: {d}")
print(f"O triplo do número é: {t}")
print(f"A raiz quadrada do valor é: {rq}")