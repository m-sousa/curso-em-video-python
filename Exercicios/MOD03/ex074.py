# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
#                       e colocar em uma tupla. Depois disso, mostre a listagem
#                       de números gerados e também indique o menor e o maior
#                       valor que estão na tupla.

from random import randint

numeros = (randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000))

print(f'''Os números gerados foram: {numeros}
O menor valor é: {sorted(numeros)[0]}
O maior valor é: {sorted(numeros)[-1]}''')
