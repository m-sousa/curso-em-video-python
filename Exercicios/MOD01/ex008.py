# Exercício Python 008: Escreva um programa que leia um valor em metros e o
#                       exiba convertido em centímetros e milímetros.

m = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'
.format(m, m/pow(10,3), m/pow(10,2), m/10, m*10, m*pow(10,2), m*pow(10,3)))
