# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na
#                       tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = radians(float(input('Digite o ângulo que você deseja: ')))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin(angulo)))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(angulo, cos(angulo)))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tan(angulo)))
