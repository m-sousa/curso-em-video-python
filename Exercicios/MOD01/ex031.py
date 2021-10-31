distancia = float(input('Qual é a distâncisa da sua viagem? '))
valor_km = 0.50 if distancia <= 200 else 0.45
print("""Você está prestes a começar uma viagem de {:.2f}.
E o preço da sua passagem será de R${:.2f}""".format(distancia, distancia * valor_km))