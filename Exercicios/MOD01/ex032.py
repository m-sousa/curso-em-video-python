from datetime import datetime

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.now().year

print('O ano {} {} BISSEXTO'.format(ano, 'é' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'NÃO é'))