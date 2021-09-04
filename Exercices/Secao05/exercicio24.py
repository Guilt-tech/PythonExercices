print('Digite o preço do produto e o estado(1-4), para ver qual o preço cobrado')
print('1- MG 7%; \n'
        '2- SP 12%; \n'
        '3- RJ 15%; \n'
        '4- MS 8% \n')
preco = float(input('Preço: '))
estado = int(input('Estado: '))
if estado == 1:
    imposto = preco * (7/100)
    precofinal = preco + imposto
    print(f'O preço final do produto no estado de MG é: {precofinal:.2f}') 
elif estado == 2:
    imposto1 = preco * (12/100)
    precofinal1 = preco + imposto1
    print(f'O preço final do produto no estado de SP é: {precofinal1:.2f}') 
elif estado == 3:
    imposto2 = preco * (15/100)
    precofinal2 = preco + imposto2
    print(f'O preço final do produto no estado de RJ é: {precofinal2:.2f}') 
elif estado == 4:
    imposto3 = preco * (8/100)
    precofinal3 = preco + imposto3
    print(f'O preço final do produto no estado de MS é: {precofinal3:.2f}')
else:
    print('Estado não existente') 