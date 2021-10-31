# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na
#                       tela o seu tipo primitivo e todas as informações
#                       possíveis sobre ele.

value = input('Digite algo: ')

print('O tipo primitivo deste valor é {}'.format(type(value)))
print('Só tem espaços? {}'.format(value.isspace()))
print('É um número? {}'.format(value.isnumeric()))
print('É alfabético? {}'.format(value.isalpha()))
print('É alfanumérico? {}'.format(value.isalnum()))
print('Está em maiúsculas? {}'.format(value.isupper()))
print('Está em minúsculas? {}'.format(value.islower()))
print('Está capitalizada? {}'.format(value.istitle()))
