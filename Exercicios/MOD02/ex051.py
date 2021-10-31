# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a
#                       razão de uma PA. No final, mostre os 10 primeiros termos
#                       dessa progressão.

a1 = int(input('Informe o primeiro termo (a1) da PA: '))
r = int(input('Informe a razão (r) da PA: '))

for i in range(1, 11):
    print(a1)
    a1 += r
