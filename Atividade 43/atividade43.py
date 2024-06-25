"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
# Solicita ao usuário que digite o peso (em kg) e a altura (em metros)
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Determina o status do IMC e exibe a mensagem apropriada
if imc < 18.5:
    status = "Abaixo do peso"
elif 18.5 <= imc < 25:
    status = "Peso ideal"
elif 25 <= imc < 30:
    status = "Sobrepeso"
elif 30 <= imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade mórbida"

# Exibe o IMC e o status
print(f"Seu IMC é {imc:.2f} e seu status é: {status}")
