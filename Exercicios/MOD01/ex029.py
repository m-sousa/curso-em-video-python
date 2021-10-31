# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
#                       Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
#                       que ele foi multado. A multa vai custar R$7,00 por cada
#                       Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('Você foi multado em R${:.2f} pois excedeu o limite de velocidade que é de 80Km/h'.format((velocidade - 80)*7))

print('Tenha um bom dia! Dirija com segurança!')
