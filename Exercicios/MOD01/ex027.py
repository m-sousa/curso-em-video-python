nome = str(input('Digite seu nome completo: ')).strip().split()

print("""Muito prazer em te conhecer!
Seu primeiro nome é {}
Seu último nome é {}""".format(nome[0], nome[len(nome) -1]))