# Exercício Python 042: Refaça o DESAFIO 35 dos triângulos, acrescentando o
#                       recurso de mostrar que tipo de triângulo será formado:
#                           – EQUILÁTERO: todos os lados iguais
#                           – ISÓSCELES: dois lados iguais, um diferente
#                           – ESCALENO: todos os lados diferentes

a = float(input('1º segmento: '))
b = float(input('2º segmento: '))
c = float(input('3º segmento: '))

if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a != b != c:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓCELES'
    
    print('Os segmentos acima PODEM FORMAR um triângulo {}'.format(tipo))
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
