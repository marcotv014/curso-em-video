"""
Crie um programa que faça o computador jogar jokenpô com você.
- pedra
- papel
- tesoura
"""
import random

# Função para determinar o vencedor
def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        return "Você venceu!"
    else:
        return "Computador venceu!"

# Lista de opções
opcoes = ["pedra", "papel", "tesoura"]

# Solicita a escolha do usuário
escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

# Verifica se a escolha do usuário é válida
if escolha_usuario not in opcoes:
    print("Escolha inválida. Tente novamente.")
else:
    # Escolha aleatória do computador
    escolha_computador = random.choice(opcoes)
    
    # Exibe as escolhas
    print(f"\nVocê escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")
    
    # Determina e exibe o vencedor
    resultado = determinar_vencedor(escolha_usuario, escolha_computador)
    print(f"\nResultado: {resultado}")
