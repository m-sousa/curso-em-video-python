# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo
#                       teclado e guarde-os em uma tupla. No final, mostre:
#                           A) Quantas vezes apareceu o valor 9.
#                           B) Em que posição foi digitado o primeiro valor 3.
#                           C) Quais foram os números pares.

valores = (
    (int(input('Informe o primeiro valor: '))),
    (int(input('Informe o segundo valor: '))),
    (int(input('Informe o terceiro valor: '))),
    (int(input('Informe o quarto valor: '))),
)

posicao_tres = 'O número 3 não foi informado'
if 3 in valores:
    posicao_tres = f'O primeiro número três está na posição {valores.index(3) + 1}'

pares = ''
for i in valores:
    if i % 2 == 0:
        pares += str(i) + ', '

if pares != '':
    pares = f'Número(s) par(es) {pares[:-2]}'
else:
    pares = 'Nenhum número par foi informado'

print(f'''
O número 9 apareceu {valores.count(9)} vezes
{posicao_tres}
{pares}
''')