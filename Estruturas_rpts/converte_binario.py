# converter um número binário em um número decimal, recebendo de entrada um número e binário e no final mostrando ele em inteiro

numero = input()
decimal = 0

for i in range(len(numero)):
    bit = int(numero[i])
    potencia = len(numero) - i - 1
    
    conta = bit * (2 ** potencia)
    decimal += conta
    
    print(f'{bit} * {2 ** potencia} = {conta}')
print(f'O número binário {numero} em decimal é {decimal}')
