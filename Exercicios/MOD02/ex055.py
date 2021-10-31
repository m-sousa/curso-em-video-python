# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No
#                       final, mostre qual foi o maior e o menor peso lidos.

menor_peso = 0
maior_peso = 0

for i in range(1, 6):
    peso = float(input("Informe o {}º peso: ".format(i)))

    if i == 1:
        menor_peso = peso
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso

print('O menor peso informado foi {} e maior peso informado foi {}'.format(menor_peso, maior_peso))
