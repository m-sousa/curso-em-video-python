velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('Você foi multado em R${:.2f} pois excedeu o limite de velocidade que é de 80Km/h'.format((velocidade - 80)*7))

print('Tenha um bom dia! Dirija com segurança!')