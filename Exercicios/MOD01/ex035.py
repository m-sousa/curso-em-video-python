# Exercício Python 035: Desenvolva um programa que leia o comprimento de três
#                       retas e diga ao usuário se elas podem ou não formar um
#                       triângulo.

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

print('Os segmentos acima {} formar um triângulo!'
.format('PODEM' if ((a + b) > c) and ((b + c) > a) and ((a + c) > b) else 'NÃO PODEM'))
