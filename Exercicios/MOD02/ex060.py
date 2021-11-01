# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o
#                       seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input("Informe um número: "))
pos = n - 1
fat = n
msg = '10 * '


while pos != 0:
    msg += str(pos) + ' * '
    fat = fat * pos
    pos -= 1

print('{}! = {} = {}'.format(n, msg[:-3], fat))
