# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu
#                       na tela:
#                           [ 1 ] somar
#                           [ 2 ] multiplicar
#                           [ 3 ] maior
#                           [ 4 ] novos números
#                           [ 5 ] sair do programa
#                       Seu programa deverá realizar a operação solicitada em
#                       cada caso.

operacao = int(0)

a = float(input('Informe o 1º número: '))
b = float(input('Informe o 2º número: '))

while operacao != 5:
    operacao = int(input('''Qual das operações abaixo deseja realizar:

    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa\n\nOperação: '''))

    if operacao in [1,2,3,4,5]:
        if operacao == 1:
            print('A soma entre {} e {} é: {}'.format(a, b, a + b))
        elif operacao == 2:
            print('A muliplicação entre {} e {} é: {}'.format(a, b, a * b))
        elif operacao == 3:
            if a > b:
                print('{} é maior que {}'.format(a, b))
            elif b > a:
                print('{} é maior que {}'.format(b, a))
            else:
                print('{} e {} são iguais'.format(a, b))
        elif operacao == 4:
            a = float(input('Informe o 1º número: '))
            b = float(input('Informe o 2º número: '))
       
print('Programa encerrado...')