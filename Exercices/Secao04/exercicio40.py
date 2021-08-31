print('Digite o números de dias que o encanador trabalhou, sendo que ele é contratado à R$30.00 por dia e são descontados 8% de impposto de renda')
dias = int(input('Dia(s): '))
valor = 30.00 * dias
descontados = valor * (8 / 100)
total = valor - descontados
print(f'O encanador receberá: R${total:.2f}')