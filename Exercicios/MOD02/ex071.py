# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa
#                       eletrônico. No início, pergunte ao usuário qual será o
#                       valor a ser sacado (número inteiro) e o programa vai
#                       informar quantas cédulas de cada valor serão entregues.
#                       OBS: considere que o caixa possui cédulas de R$50, R$20,
#                            R$10 e R$1.

from math import trunc

acc_50 = 0
acc_20 = 0
acc_10 = 0
acc_01 = 0

valor = int(input('Informe o valor do saque (sem centavos) R$ '))


if valor >= 50:
    acc_50 = trunc(valor / 50)
    valor = valor - (acc_50 * 50)

if valor >= 20:
    acc_20 = trunc(valor / 20)
    valor = valor - (acc_20 * 20)

if valor >= 10:
    acc_10 = trunc(valor / 10)
    valor = valor - (acc_10 * 10)

if valor >= 1:
    acc_01 = trunc(valor / 1)

print(f'''
{acc_50:4} notas de R$ 50
{acc_20:4} notas de R$ 20
{acc_10:4} notas de R$ 10
{acc_01:4} notas de R$ 1
''')
