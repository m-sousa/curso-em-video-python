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
