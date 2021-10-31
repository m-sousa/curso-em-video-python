salario = float(input('Qual é o salário do funcionário? R$'))

fator = 0.15 if salario<= 1250 else 0.1

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, salario + (salario*fator)))