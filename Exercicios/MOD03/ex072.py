# Exercício Python 072: Crie um programa que tenha uma dupla totalmente
#                       preenchida com uma contagem por extenso, de zero até
#                       vinte. Seu programa deverá ler um número pelo teclado
#                       (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Informe um número de 0 a 20: '))
    if n >= 0 and n <=20:
        break

print(f'O número {n} por extenso é {numeros[n]}')