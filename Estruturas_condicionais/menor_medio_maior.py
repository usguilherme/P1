# Usando apenas condicionais, escreve um programa que lê e ordena 3 números inteiros

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b and a >= c:
    maior = a
    if b <= c:
        menor = b
        meio = c
    else:
        menor = c
        meio = b
elif b >= a and b >= c:
    maior = b
    if a <= c:
        menor = a
        meio = c
    else:
        menor = c
        meio = a
else:
    maior = c
    if a <= b:
        menor = a
        meio = b
    else:
        menor = b
        meio = a

print(f'Os números ordenados são:, {menor}, {meio}, {maior}')
