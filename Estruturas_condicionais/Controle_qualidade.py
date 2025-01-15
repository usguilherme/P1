# O PROCON designou uma equipe de controle de qualidade para verificar a porcentagem de água no peso total do produto, com a tolerancia de 10%
# isto é se menos de 10% do peso de uma carne congelado for de água, o produto é considerado em "conformidade", se for menos de 5% ganha um selo de "Produto Qualis A"
# Caso contrário, o produto é considerado "não conforme"

peso_antes = float(input())
peso_depois = float(input())
porcentagem = 100 - ((peso_depois / peso_antes) * 100)
definicao = ''

if porcentagem < 5:
    definicao = 'Produto qualis A'
elif porcentagem < 10:
    definicao = 'Produto em conformidade'
else:
    definicao = 'Produito em conforme'

print(f'{definicao:.1f}% do peso do produto é de água congelada')
print(definicao)
