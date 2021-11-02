# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
#                       (não usar acentos). Depois disso, você deve mostrar,
#                       para cada palavra, quais são as suas vogais.

palavras = ('Ana', 'Maria', 'Braga', 'Bola', 'Sapo', 'Papel')

for p in palavras:
    print(f'{p}: ', end='')
    vogais = ''
    for l in p:
        if l in 'aAeEiIoOuU':
            vogais += f'{l}, '
    print(vogais[:-2])
