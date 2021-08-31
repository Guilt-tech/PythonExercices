print('Digite o valor do produto e este receberá: 10% de desconto, o valor do parcelamento em 3 vezes sem juros, a comissão do vendedor caso da compra seja à vista (5% do valor do produto com desconto) e a comissão do vendedor caso a compra seja parcelada (5% do valor do produto')
produto = float(input('Preço: '))
desconto = produto * (10 / 100)
produto_desconto = produto - desconto
parcelado = produto / 3
comissao_a_vista = produto_desconto * (5 / 100)
comissao_parcelado = produto * (5 / 100)
print(f'O produto com desconto de 10% é: R${produto_desconto:.2f} e sem desconto era: R${produto:.2f}.\n '
      f'O valor das 3 parcelas fica: R${parcelado:.2f}.\n'
      f'A comissão do vendedor (compra realizada à vista) é: R${comissao_a_vista:.2f}.\n'
      f'A comissão do vendedor (compra realizada parcelado) é: R${comissao_parcelado:.2f}. ')