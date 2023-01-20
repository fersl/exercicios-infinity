valor_compra = float(input('Digite o valor da compra: R$'))
porcentagem_desconto = 0
valor_desconto = 0

if (valor_compra >= 500):
	porcentagem_desconto = ((valor_compra - 500) // 100) + 0.01

	if (porcentagem_desconto <= 0.25):
		# desconto cumulativo até 25%
		valor_desconto = porcentagem_desconto * valor_compra
	else:
		# passou do máximo de 25%
		valor_desconto = 0.25 * valor_compra

valor_final = valor_compra - valor_desconto

print('---------------------------------------------------------')
print(f' Valor da Compra: R${valor_compra:.2f}')
print(f' Porcentagem de Desconto: {porcentagem_desconto:.0%}')
print('---------------------------------------------------------')
print(f' Valor Final: R${valor_final:.2f}')
print('---------------------------------------------------------')