# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
#                       um de cada vez, para cada valor digitado pelo usuário. O
#                       programa será interrompido quando o número solicitado
#                       for negativo.

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break

    print('-' * 12)

    for i in range(1, 11):
        print(f'{n} X {i:2} = {n * i:2}')

    print('-' * 12)
