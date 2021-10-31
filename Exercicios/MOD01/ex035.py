a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

print('Os segmentos acima {} formar um triângulo!'.format('PODEM' if ((a + b) > c) and ((b + c) > a) and ((a + c) > b) else 'NÃO PODEM'))