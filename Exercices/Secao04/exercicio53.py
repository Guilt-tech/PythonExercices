print('Digite as dimensões do terreno comprimento e largura e o preço do metro da tela')
c = float(input('Comprimento: '))
l = float(input('Largura: '))
p = float(input('Preço da tela por metro: '))
tamanho = c * l
preco = tamanho * p
print(f'O preço para cercar esse terreno com tela é: {preco}')