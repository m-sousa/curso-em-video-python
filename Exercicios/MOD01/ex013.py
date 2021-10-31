# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e
#                       mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))

print('Um funcionário que ganhava R${}, com 15% de aumento, passa a recever R${:.2f}'
.format(salario, salario + (salario * 15 / 100)))
