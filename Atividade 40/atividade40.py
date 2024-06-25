"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0:
Reprovado

- Média entre 5.00 e 6.9:
Recuperação

- Média 7.0 ou superior:
Aprovado
"""
# Solicita ao usuário que digite as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Determina a situação do aluno e exibe a mensagem apropriada
if media < 5.0:
    print(f"Média: {media:.2f} - Reprovado")
elif 5.0 <= media <= 6.9:
    print(f"Média: {media:.2f} - Recuperação")
else:
    print(f"Média: {media:.2f} - Aprovado")
