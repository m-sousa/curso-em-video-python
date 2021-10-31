#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio
#                      de um arquivo MP3.

import pathlib
import pygame

pygame.init()
pygame.mixer.music.load(pathlib.Path(__file__).parent.resolve().joinpath('ex021.mp3'))
pygame.mixer.music.play()

input('Digite algo para parar...')
