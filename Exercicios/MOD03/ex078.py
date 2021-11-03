# Exercício Python 078: Faça um programa que leia 5 valores numéricos e
#                       guarde-os em uma lista. No final, mostre qual foi o
#                       maior e o menor valor digitado e as suas respectivas
#                       posições na lista.

valores = []

for v in range(0,5):
    valores.append(int(input('Informe um valor: ')))

maior = max(valores)
menor = min(valores)

print(f'''O maior valor informado foi {maior} e sua posição é {valores.index(maior) + 1}
O menor valor informado foi {menor} e sua posição é {valores.index(menor) + 1}''')
