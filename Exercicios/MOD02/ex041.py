# Exercício Python 041: A Confederação Nacional de Natação precisa de um
#                       programa que leia o ano de nascimento de um atleta e
#                       mostre sua categoria, de acordo com a idade:
#                           – Até 9 anos: MIRIM
#                           – Até 14 anos: INFANTIL
#                           – Até 19 anos: JÚNIOR
#                           – Até 25 anos: SÊNIOR
#                           – Acima de 25 anos: MASTER

from datetime import datetime

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    classificacao = 'JUNIOR'
elif idade <=14:
    classificacao = 'INFANTIL'
elif idade <=19:
    classificacao = 'JUNIOR'
elif idade <=25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'

print('O atleta tem {} anos.\nClassificação: {}'.format(idade, classificacao))
