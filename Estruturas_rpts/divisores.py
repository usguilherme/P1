# Divisores próprios, o programa recebe um numero de entrada, e o exibe os divisores naturais do proprio número de entrada

numero = int(input())

for i in range(1, numero + 1):
    if numero % i == 0 and i < numero:
        print(i)
