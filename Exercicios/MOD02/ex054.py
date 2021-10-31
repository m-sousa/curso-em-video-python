# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete
#                       pessoas. No final, mostre quantas pessoas ainda não
#                       atingiram a maioridade e quantas já são maiores.

from datetime import datetime

acc_maiores = 0
acc_menores = 0

for i in range(1, 8):
    ano_nascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '
    .format(i)))
    
    if datetime.now().year - ano_nascimento < 18:
        acc_menores += 1
    else:
        acc_maiores += 1

print('Das 7 pessoas informadas, {} não menores de idade e {} são maiores de idade'
.format(acc_menores, acc_maiores))
