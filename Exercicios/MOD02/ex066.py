# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
#                       O programa só vai parar quando o usuário digitar o valor
#                       999, que é a condição de parada. No final, mostre
#                       quantos números foram digitados e qual foi a soma entre
#                       elas (desconsiderando o flag).

n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Informe um número (999 para sair): '))

    if n == 999:
        break

    contador += 1
    soma += n

print(f'Você informou {contador} números e a soma entre eles é {soma}')