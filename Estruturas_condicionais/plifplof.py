# Programa que receba três números de entradas e calcule o somatório deles, o programa imprime 'plif' se este somatório for divisível por 3
# ou 'plof' se for divisível por 5. se for divisível por ambos, imprima 'plifplof'. caso não seja divisível por nenhum, imprima o somatório

n1 = int(input())
n2 = int(input())
n3 = int(input())
somatorio = n1 + n2 + n3

if somatorio % 3 == 0 and somatorio % 5 == 0:
    print('plifplof')
elif somatorio % 3 == 0:
    print('plif')
elif somatorio % 5 == 0:
    print('plof')
