# Exercício Python 061: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de
#                       uma PA, mostrando os 10 primeiros termos da progressão
#                       usando a estrutura while.

termo = int(input('Informe o primeiro termo (a1) da PA: '))
r = int(input('Informe a razão (r) da PA: '))
pos = 1
pa = []

while pos <= 10:
    pa.append(termo)
    termo += r
    pos += 1

print(pa)
