# Exercício Python 070: Crie um programa que leia o nome e o preço de vários
#                       produtos. O programa deverá perguntar se o usuário vai
#                       continuar ou não. No final, mostre:
#                           A) qual é o total gasto na compra;
#                           B) quantos produtos custam mais de R$1000;
#                           C) qual é o nome do produto mais barato.

total = 0
acc_prod_mais_mil = 0
nome_prod_mais_barato = ''
valor_prod_mais_barato = 0

while True:
    nome = str(input('Informe o nome do produto: ')).strip()
    valor = float(input('Informe o valor do produto: R$ '))

    total += valor
    
    if valor > 1000:
        acc_prod_mais_mil += 1

    if valor < valor_prod_mais_barato or valor_prod_mais_barato == 0:
        nome_prod_mais_barato = nome
        valor_prod_mais_barato = valor

    continuar = 'A'
    while continuar not in ['S', 'N']:
        continuar = str(input('Continuar a compra (S/N): ')).strip().upper()
    
    if continuar == 'N':
        break

print(f'''
O valor total da compra foi R${total:.2f}
{acc_prod_mais_mil} produtos custaram mais de R$1000.00
O produto mais barato foi {nome_prod_mais_barato}
''')
