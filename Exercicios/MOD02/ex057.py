# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só
#                       aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
#                       digitação novamente até ter um valor correto.

sexo = ''

while sexo.upper() not in ['M', 'F']:
    sexo = str(input('Informe o sexo (M/F): ')).strip()

print('Fim')
