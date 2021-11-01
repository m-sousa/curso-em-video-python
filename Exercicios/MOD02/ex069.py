# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias
#                       pessoas. A cada pessoa cadastrada, o programa deverá
#                       perguntar se o usuário quer ou não continuar. No final,
#                       mostre:
#                           A) quantas pessoas tem mais de 18 anos;
#                           B) quantos homens foram cadastrados;
#                           C) quantas mulheres tem menos de 20 anos.

acc_mais_18 = 0
acc_homens = 0
acc_mulhetes_menos_20 = 0

while True:
    idade = int(input('Informe a idade: '))
    
    sexo = 'A'
    while sexo not in ['M','F']:
        sexo = str(input('Informe o sexo (M/F): ')).strip().upper()

    if idade > 18:
        acc_mais_18 += 1
    
    if sexo == 'M':
        acc_homens += 1
    elif idade < 20:
        acc_mulhetes_menos_20 += 1
    
    continuar = 'A'
    while continuar not in ['S', 'N']:
        continuar = str(input('Continuar (S/N)')).strip().upper()

    if continuar == 'N':
        break

print(f'''Total de pessoas +18: {acc_mais_18}
Total de homens: {acc_homens}
Total de mulheres -20: {acc_mulhetes_menos_20}''')
