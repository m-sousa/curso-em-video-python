# Exercício Python 020: O mesmo professor do desafio 19 quer sortear a ordem de 
#                       apresentação de trabalhos dos alunos. Faça um programa
#                       que leia o nome dos quatro alunos e mostre a ordem
#                       sorteada.

from random import shuffle

alunos = []

alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Terceiro aluno: '))
alunos.append(input('Quarto aluno: '))

shuffle(alunos)

print('A ordem de apresentação será {}'.format(alunos))
