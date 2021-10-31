# Exercício Python 052: Faça um programa que leia um número inteiro e diga se
#                       ele é ou não um número primo.

n = int(input('Informe um número inteiro: '))

acc = 0

for i in range(n, 0, -1):
    if n % i == 0:
        acc += 1

print('O número {} {} primo'.format(n, 'É' if acc == 2 else 'NÃO É'))