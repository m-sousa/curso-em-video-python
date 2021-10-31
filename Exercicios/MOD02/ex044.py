# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por
#                       um produto, considerando o seu preço normal e condição
#                       de pagamento:
#                           – à vista dinheiro/cheque: 10% de desconto
#                           – à vista no cartão: 5% de desconto
#                           – em até 2x no cartão: preço formal 
#                           – 3x ou mais no cartão: 20% de juros

print('=' * 10 + ' LOJAS SOUSA ' + '=' * 10)
preco = float(input('Preço das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Informe a sua opção: '''))

if opcao in [1,2,3,4]:
    if opcao == 1:
        total = preco - (preco * 0.1)
    elif opcao == 2:
        total = preco - (preco * 0.05)
    elif opcao == 3:
        total = preco
    else:
        total = preco + (preco * 0.2)

    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    print('Opçao inválida')
