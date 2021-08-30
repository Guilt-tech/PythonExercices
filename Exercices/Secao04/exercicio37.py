print('Digite o valor de um produto e este irá receber 12% de desconto')
valor = float(input())
desconto = valor * (12/100)
valor_com_desconto = valor - desconto
print(f'O novo valor com o desconto será: {valor_com_desconto} e o preço antigo era: {valor}')