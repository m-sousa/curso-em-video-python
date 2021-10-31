# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre
#                       uma mensagem de boas-vindas.

nome = str(input('Qual é o seu nome? ')).strip()
print('Prazer em te conhecer, {}'.format(nome))
