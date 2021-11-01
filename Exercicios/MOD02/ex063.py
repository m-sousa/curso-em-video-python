# Exercício Python 063: Escreva um programa que leia um número N inteiro
#                       qualquer e mostre na tela os N primeiros elementos de
#                       uma Sequência de Fibonacci. Exemplo:
#                           0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Informe um número: '))

pos = 2
a=0
b=1
fibo = '0 - 1 - '

while pos < n:
    c = a + b
    a = b
    b = c
    fibo += str(c) + ' - ' 
    pos += 1

print('Fibonacci: {}'.format(fibo[:-3]))
