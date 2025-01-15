# Escreva um programa que verifica se um ano é bissexto ou não.
# Um ano é bissexto se for divisível por 400 oiu se for divisível por 4 e não por 100.
# A entrada consiste em um único valor inteiro correspondendo ao ano que deve ser verificado.
# A saída consiste em uma única linha que diz se o ano é ou não é bissexto.

ano = int(input())
if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
