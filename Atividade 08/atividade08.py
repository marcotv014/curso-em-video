"""
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
"""
# Aqui coloquei uma breve informação para o usuario pois muita das vezes ele não sabe sobre.
print("Ola, para o bom funcionamento do sistema, por gentileza!")
print("Usar . para a , para informar o numero quebrado como ex: 1.5 para um metro e meio!")
# aqui irei pegar a medida em metros para converter.
n1 = float(input("Digite a metragem: "))
# aqui irei fazer o sistema que ira converter para as demais medidas.
ce = n1 * 100 # para ver o centimetro
mi = ce * 100 # para ver o milimetro
# aqui irei retornar as medidas para o usuáro
print(f"A metragem informada foi de {n1}")
print(f"Em centimetro é {ce}")
print(f"Em milimetro é {mi}")