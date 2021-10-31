# Exercício Python 009: Refaça o DESAFIO 9, mostrando a tabuada de um número que
#                       o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um nº para ver sua tabuada: '))

for i in range(1, 11):
    print('{} X {:2} = {:2}'.format(n, i, n * i))
