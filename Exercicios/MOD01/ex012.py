# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e
#                       mostre seu novo preço, com 5% de desconto.

valor = float(input('Qual é o preço do produto: R$'))
desconto = valor * 5 / 100
print('O valor do produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'
.format(valor, valor - desconto))
