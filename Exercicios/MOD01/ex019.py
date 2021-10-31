# Exercício Python o19: Um professor quer sortear um dos seus quatro alunos para 
#                       apagar o quadro. Faça um programa que ajude ele, lendo o
#                       nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

alunos = []

alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Terceiro aluno: '))
alunos.append(input('Quarto aluno: '))

print('O aluno escolhido foi {}'.format(choice(alunos)))
