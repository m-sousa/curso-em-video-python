salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 15 / 100
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a recever R${:.2f}'.format(salario, salario + aumento))