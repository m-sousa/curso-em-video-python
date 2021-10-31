# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de
#                       4 pessoas. No final do programa, mostre:
#                           - a média de idade do grupo;
#                           - qual é o nome do homem mais velho;
#                           - quantas mulheres têm menos de 20 anos.

acc_idade = 0
nome_h_mais_velho = 'Não informado'
idade_h_mais_velho = 0
qtd_m_menos_20 = 0

for i in range(1,5):
    print('Dados da {}ª pessoa'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()

    acc_idade += idade

    if sexo == 'M':
        if idade > idade_h_mais_velho:
            idade_h_mais_velho = idade
            nome_h_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            qtd_m_menos_20 += 1

print('''Resumo dos dados
Média de idade do grupo: {}
O nome do homem mais velho: {}
Quantidade de mulhetes -20: {}'''.format(acc_idade/4, nome_h_mais_velho, qtd_m_menos_20))

    
