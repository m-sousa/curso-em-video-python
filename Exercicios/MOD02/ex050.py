# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
#                       mostre a soma apenas daqueles que forem pares. Se o
#                       valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for i in range(1, 7):
    valor = int(input('Informe o {}º valor: '.format(i)))
    if valor % 2 == 0:
        contador += 1
        soma += valor

print('O total dos {} valores PARES informados é de {}'.format(contador, soma))
