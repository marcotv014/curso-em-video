"""
Faça um programa em python que abra e reproduza o áudio de um arquivo mp3
"""
# Biblioteca usada
import pygame
# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
arquivo_mp3 = "seu_arquivo.mp3"
pygame.mixer.music.load(arquivo_mp3)

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música está tocando
while pygame.mixer.music.get_busy():
    pass