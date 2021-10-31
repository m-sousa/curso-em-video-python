# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se
#                       ela é um palíndromo, desconsiderando os espaços.
#                       Exemplos de palíndromos:

texto = str(input('Informe um texto: ')).strip()
alt = ''

for l in range(len(texto) - 1, -1, -1):
    alt += texto[l]

print('O texto informado {} um palindromo'
.format('É' if texto.replace(' ', '') == alt.replace(' ', '') else 'NÃO É'))
