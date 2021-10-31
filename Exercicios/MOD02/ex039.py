# Exercício Python 039: Faça um programa que leia o ano de nascimento de um
#                       jovem e informe, de acordo com a sua idade, se ele ainda
#                       vai se alistar ao serviço militar, se é a hora exata de 
#                       se alistar ou se já passou do tempo do alistamento. Seu
#                       programa também deverá mostrar o tempo que falta ou que
#                       passou do prazo.

from datetime import datetime

ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))

if  idade < 18:
    print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.'.format(18-idade, ano_atual + (18-idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(idade-18, ano_atual - (idade-18)))
else:
    print('Você tem que se alistar imediatamente')
