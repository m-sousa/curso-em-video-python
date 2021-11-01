# Exercício Python 068: Faça um programa que jogue par ou ímpar com o
#                       computador. O jogo só será interrompido quando o jogador
#                       perder, mostrando o total de vitórias consecutivas que
#                       ele conquistou no final do jogo.

from random import randint

acc_vitorias = 0
j_op = 'A'
is_int = False

while True:
    c_num = randint(0, 10)

    while j_op not in 'IP':
        j_op = str(input('PAR ou ÍMPAR (P/I): ')).strip().upper()
    
    j_num = int(input('Informe um número: '))

    soma = (c_num + j_num)
    par = soma % 2 == 0

    print(f'Eu escolhi {c_num} e você {j_num}, somando {soma} que é {"" if par else "ÍM"}PAR')

    if (par and j_op == 'P') or (not par and j_op == 'F'):
        acc_vitorias += 1
    else:
        break

print(f'Você venceu {acc_vitorias} vezes seguidas.')
