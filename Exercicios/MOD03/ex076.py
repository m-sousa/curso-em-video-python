# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de
#                       produtos e seus respectivos preços, na sequência. No
#                       final, mostre uma listagem de preços, organizando os
#                       dados em forma tabular.

produtos = ('Pão de forma', 8.75,
            'Pão de alho', 12.50,
            'Farinha de trigo', 5.59,
            'Arroz parbolizado', 6.87,
            'Feijão carioca', 8.99)

print(' MERCADINHO SOUSA '.center(50,"="))

for i, p in enumerate(produtos):
    if i == 0 or i % 2 == 0:
        print(f'{p:.<39}', end='')
    else:
        print(f' R$ {p:>7.2f}')
        
print(''.center(50,"="))
