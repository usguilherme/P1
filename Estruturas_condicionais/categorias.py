# Escreva um programa que com base na idade de um nadador determina em que categoria ele irá competir

# Infantil A - 5 a 7 anos
# Infantil B - 8 a 10 anos
# Juvenil A - 11 a 13 anos
# Juvenil A - 14 a 17 anos
# Senior - Acima de 17 anos

nome = input()
idade = int(input())
categoria = ''

if 5 <= idade <= 7:
    categoria = 'Infantil A'
elif 8 <= idade <= 10:
    categoria = 'Infantil B'
elif 11 <= idade <= 13:
    categoria = 'Juvenil A'
elif 13 <= idade <= 17:
    categoria = 'Juvenil B'
elif idade > 17:
    categoria = 'Senior'
else:
    categoria = 'Não pode competir'

print(f'{nome}, {idade} anos, {categoria}')
