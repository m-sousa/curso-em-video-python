#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e 
#                      mostre: 
#                      a. O nome com todas as letras maiúsculas e minúsculas.
#                      b. Quantas letras ao todo (sem considerar espaços).
#                      c. Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('''Análisando seu nome...
Seu nome em maíusculas é {}
Seu nome em minúsculas é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras
'''.format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), nome.split()[0], len(nome.split()[0])))
