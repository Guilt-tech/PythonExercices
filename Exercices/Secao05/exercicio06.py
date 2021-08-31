print('Digite dois números, para ver qual é o maior entre eles e a sua diferença')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
if n1 > n2:
    diferenca = n1 - n2
    print(f'O primeiro número {n1} é maior que o segundo número {n2} e a sua diferença é de: {diferenca}')
else:
    diferenca1 = n2 - n1
    print(f'O segundo número {n2} é maior que o primeiro número {n1} e a sua diferença é de: {diferenca1}')