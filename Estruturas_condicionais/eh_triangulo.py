# Para ser um triangulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e 
# maior que o valor absoluto da diferença entre essas medida, escreva um programa que receba os lados e veja se é um triangulo válido ou não

l1 = int(input())
l2 = int(input())
l3 = int(input())
soma = l1 + l2 + l3

if l1 < l2 + l3 and l1 > abs(l2 - l3):
    print(f'triangulo valido. {soma}')
elif l2 < l1 + l3 and l2 > abs(l1 - l3):
    print(f'triangulo valido. {soma}')
elif l3 < l2 + l1 and l3 > abs(l2 - l1):
    print(f'triangulo valido. {soma}')
else:
    print(f'triangulo invalido.')
