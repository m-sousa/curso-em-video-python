# Exercício Python 014: Escreva um programa que converta uma temperatura 
#                       digitando em graus Celsius e converta para graus 
#                       Fahrenheit.

celsius = float(input('Informe a temperatura em ºC: '))

print('A temperatura de {}ºC corresponde a {:.1f}ºF!'
.format(celsius, celsius * 9 / 5 + 32))
