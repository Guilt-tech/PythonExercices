print('Digite um ano, para ver se ele é bissexto')
ano = int(input('Ano: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')