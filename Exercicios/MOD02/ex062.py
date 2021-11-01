# Exercício Python 062: Melhore o DESAFIO 61, perguntando para o usuário se ele
#                       quer mostrar mais alguns termos. O programa encerrará
#                       quando ele disser que quer mostrar 0 termos.

termo = int(input('Informe o primeiro termo (a1) da PA: '))
r = int(input('Informe a razão (r) da PA: '))
quantidade = 10

while quantidade != 0:
    pa = [] 
    pos = 1
    while pos <= quantidade:
        pa.append(termo)
        termo += r
        pos += 1
    print(pa)
    quantidade = int(input('Mostrar mais quantos termos: '))
