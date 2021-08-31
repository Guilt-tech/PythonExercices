print('Digite dois números, para ver qual o maiore se eles são iguais')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
if n1 > n2:
    print(f'O primeiro primeiro {n1} é maior que o segundo número {n2}')
elif n2 > n1:
    print(f'O segundo {n2} é maior que o primeiro {n1}')
else:
    print(f'Os números {n1} e {n2} são iguais')