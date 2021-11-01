# Exercício Python 064: Crie um programa que leia vários números inteiros pelo
#                       teclado. O programa só vai parar quando o usuário
#                       digitar o valor 999, que é a condição de parada. No
#                       final, mostre quantos números foram digitados e qual foi
#                       a soma entre eles (desconsiderando o flag).

n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Informe um número (999 para sair): '))
    if n != 999:
        contador += 1
        soma += n

print('Você informou {} números e a soma entre eles é {}'.format(contador, soma))
