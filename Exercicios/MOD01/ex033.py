lista = []

lista.append(int(input('Primeiro valor: ')))
lista.append(int(input('Segundo valor: ')))
lista.append(int(input('Terceiro valor: ')))

lista.sort()

print("""O menor valor digitado foi {}
o maior valor digitado foi {}""".format(lista[0], lista[2]))