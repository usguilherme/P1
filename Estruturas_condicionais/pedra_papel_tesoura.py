# Pedra, Papel e Tesoura, com o computador

import random

print("Bem-vindo ao jogo Pedra, Papel e Tesoura do Guilherme")

print("Escolha uma dessas opçoes")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

usuario = int(input("Digite o número correspondente à sua escolha: "))
computador = random.randint(1, 3)

if usuario == 1:
    escolha_usuario = "Pedra"
elif usuario == 2:
    escolha_usuario = "Papel"
elif usuario == 3:
    escolha_usuario = "Tesoura"

if computador == 1:
    escolha_computador = "Pedra"
elif computador == 2:
    escolha_computador = "Papel"
elif computador == 3:
    escolha_computador = "Tesoura"


print(f'Você escolheu: {escolha_usuario}')
print(f'O computador escolheu: {escolha_computador}')

if usuario == computador:
    resultado = "Empate"
elif (usuario == 1 and computador == 3) or (usuario == 2 and computador == 1) or (usuario == 3 and computador == 2):
    resultado = "Você ganhou!"
else:
    resultado = "Você perdeu!"


print(' Resultado:", resultado')
