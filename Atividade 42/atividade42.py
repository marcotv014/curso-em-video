"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sera formado:

- Equilátero: Todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
# Solicita ao usuário que digite o comprimento das três retas
r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica se as retas podem formar um triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    # Se formarem um triângulo, determina o tipo de triângulo
    if r1 == r2 == r3:
        tipo = "Equilátero"
    elif r1 == r2 or r1 == r3 or r2 == r3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    # Exibe o resultado
    print(f"As retas podem formar um triângulo {tipo}.")
else:
    # Se não formarem um triângulo, exibe uma mensagem apropriada
    print("As retas não podem formar um triângulo.")
