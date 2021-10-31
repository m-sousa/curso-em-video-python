# Exercício Python 028: Escreva um programa que faça o computador “pensar” em um
#                       número inteiro entre 0 e 5 e peça para o usuário tentar
#                       descobrir qual foi o número escolhido pelo computador.
#                       O programa deverá escrever na tela se o usuário venceu
#                       ou perdeu.

from random import randint
from time import sleep

numero = randint(0,5)
palpite = int(input("""Vou pensar em um número entre 0 e 5.
Tente adivinhar...
Em que número pensei? """))
sleep(2)
if numero == palpite:
    print('Você acertou!')
else:
    print('Errou! eu pensei no número {} e não no {}!'.format(numero, palpite))
