numero = int(input('Informe um número: '))

milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10


print("""Analisando o número {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(numero, unidade, dezena, centena, milhar))