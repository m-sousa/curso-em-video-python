# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com
#                       você.

from random import randint
from time import sleep

jogador = int(input('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Sua jogada: '''))

if jogador in [0,1,2]:
    computador = randint(0, 2)
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    print('Minha jogada: {}'.format(computador))


    if jogador == computador:
        resultado = 'EMPATE'
    elif jogador == 0 and computador == 2: # pedra vence tesoura
        resultado = 'PEDRA vence TESOURA, você VENCEU'
    elif computador == 0 and jogador  == 2: # pedra vence tesoura
        resultado = 'PEDRA vence TESOURA, você PERDEU'
    elif jogador == 2 and computador == 1: # tesoura vence papel
        resultado = 'TESOURA vence PAPEL, você VENCEU'
    elif computador == 2 and jogador  == 1: # tesoura vence papel
        resultado = 'TESOURA vence PAPEL, você PERDEU'
    elif jogador == 1 and computador == 0: # papel vence pedra
        resultado = 'TESOURA vence PAPEL, você VENCEU'
    elif computador == 1 and jogador  == 0: # papel vence pedra
        resultado = 'TESOURA vence PAPEL, você PERDEU'

    print(resultado)

else:
    print('Opção inválida')
