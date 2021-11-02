# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados
#                       da Tabela do Campeonato Brasileiro de Futebol, na ordem
#                       de colocação. Depois mostre:
#                           a) Os 5 primeiros times.
#                           b) Os últimos 4 colocados.
#                           c) Times em ordem alfabética.
#                           d) Em que posição está o time da Chapecoense.

times = ('Atlético Mineiro - MG', 'Palmeiras - SP', 'Flamengo - RJ',
         'Red Bull Bragantino - SP', 'Fortaleza - CE', 'Corinthians - SP',
         'Internacional - RS', 'Fluminense - RJ', 'America - MG', 'Cuiabá - MT',
         'Atlético - GO', 'São Paulo -', 'Ceará - CE', 'Santos - SP', 
         'Athletico Paranaense - PR', 'Bahia - BA', 'Sport - PE',
         'Juventude - RS', 'Grêmio - RS', 'Chapecoense - SC')

print(f'''Os cinco primeiros colocados são: {times[0:6]}
Os quatro últimos colocados são: {times[-4:]}
Os times em ordem alfabética: {sorted(times)}
A chapecoense está na {times.index('Chapecoense - SC') + 1}ª posição''')
