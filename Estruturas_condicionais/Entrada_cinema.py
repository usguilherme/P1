# Software para liberação de entrada em um cinema, de acordo com a idade

# Pessoas com 16 anos ou mais podem entrar no filme livremente. Crianças com menos de 16 ew apartir de 14 podem entrar, desde que acompanhadados com seus país
# E crianças com menos de 14 anos não podem entrar de forma alguma

ano_atual = int(input('Ano atual? '))
ano_nascimento = int(input('Ano de nascimento? '))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print('idade calculada: {idade} anos')
    print('Entrada permitida')

elif 14 <= idade < 16:
    print('idade calculada: {idade} anos')
    pais = input('Com os país? ').lower()
    if pais == 's':
        print('Entrada permitida')
    else:
        print('Entrada proibida para menores de 16 anos sem os pais')
else:
    print('idade calculada: {idade} anos')
    print('Entrada proibida para menores de 14 anos')
    
