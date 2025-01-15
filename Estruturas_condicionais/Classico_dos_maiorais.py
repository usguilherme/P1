#Partida de futebol, quem será o grande vencedor? entre Treze e campinense?
#Primeira entrada é a quantidade de gols do Campinense
#Segunda entrada é a quantidade de gols do Treze

campinense = int(input())
treze = int(input())

if campinense > treze:
    print('Campinense')
elif treze > campinense:
    print('Treze')
else:
    print('Empate')
