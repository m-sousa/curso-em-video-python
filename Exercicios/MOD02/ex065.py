# Exercício Python 065: Crie um programa que leia vários números inteiros pelo
#                       teclado. No final da execução, mostre a média entre
#                       todos os valores e qual foi o maior e o menor valores
#                       lidos. O programa deve perguntar ao usuário se ele quer
#                       ou não continuar a digitar valores.

numeros = []
contador = 0
opcao = 'S'

while opcao.upper() == 'S':
    numeros.append(int(input('Informe um número: ')))
    opcao = str(input('Continuar (S/N): ')).strip()
    contador += 1

numeros.sort()

print('''A média entre os valores informados é: {}
O menor valor é: {}
O maior valor é: {}'''.format(sum(numeros)/len(numeros), numeros[0], numeros[-1]))
