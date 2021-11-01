# Exercício Python 058: Melhore o jogo do DESAFIO 28 onde o computador vai
#                       “pensar” em um número entre 0 e 10. Só que agora o
#                       jogador vai tentar adivinhar até acertar, mostrando no
#                       final quantos palpites foram necessários para vencer.

from random import randint

n = randint(0, 10)
palpite = -1
tentativas = 0

while palpite != n:
    palpite = int(input('Informe um número entre 0 e 10: '))
    tentativas += 1

print('Eu escolhi o número {} e foram necessárias {} tentativas para você adivintar'.format(n, tentativas)) 
