# Exercício Python 033: Faça um programa que leia três números e mostre qual é o
#                       maior e qual é o menor.



lista = []

lista.append(int(input('Primeiro valor: ')))
lista.append(int(input('Segundo valor: ')))
lista.append(int(input('Terceiro valor: ')))

lista.sort()

print("""O menor valor digitado foi {}
o maior valor digitado foi {}""".format(lista[0], lista[2]))