# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma
#                       pessoa, calcule seu Índice de Massa Corporal (IMC) e
#                       mostre seu status, de acordo com a tabela abaixo:
#                           – IMC abaixo de 18,5: Abaixo do Peso
#                           – Entre 18,5 e 25: Peso Ideal
#                           – 25 até 30: Sobrepeso
#                           – 30 até 40: Obesidade
#                           – Acima de 40: Obesidade Mórbida

peso = float(input('Informe o peso (Kg): '))
altura = float(input('Informe a altura (m): '))

imc = peso / (pow(altura,2))

if imc < 18.5:
    situacao = 'ABAIXO DO PESO'
elif imc < 25:
    situacao = 'PESO NORMAL'
elif imc < 30:
    situacao = 'SOBREPESO'
elif imc <= 40:
    situacao = 'OBESIDADE'
else:
    situacao = 'OBESIDADE MÓRBIDA'

print('Seu IMC é de {:.1f} e você está na faixa de {}'.format(imc, situacao))
