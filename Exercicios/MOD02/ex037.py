# Exercício Python 037: Escreva um programa em Python que leia um número inteiro
#                       qualquer e peça para o usuário escolher qual será a base
#                       de conversão: 1 para binário, 2 para octal e 3 para
#                       hexadecimal.

numero = int(input('Digite um número inteiro: '))
opcao = int(input("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: """))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'. format(numero, format(numero, "b")))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'. format(numero, format(numero, "o")))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'. format(numero, format(numero, "x")))
else:
    print('Opção inválida!')
