print('Digite um número para escolher as opções abixo')
n = int(input(('Escolha a opção: \n'
        '1- Soma de 2 número. \n'
        '2- Diferença entre 2 números (maior pelo menor). \n'
        '3- Produto entre 2 números. \n'
        '4- Divisão entre 2 números (o denominador não pode ser zero). \n'
        'Opção: ')))
if n == 1:
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    s = n1 + n2
    print(f'A soma entre {n1:.2f} e {n2:.2f} é: {s:.2f}')
elif n == 2:
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    if n1 > n2:
        sub = n1 - n2
        print(f'A diferença entre {n1:.2f} e {n2:.2f} é: {sub:.2f}')
    elif n2 > n1:
        sub1 = n2 - n1
        print(f'A diferença entre {n2:.2f} e {n1:.2f} é: {sub1:.2f}')
    else:
        print('Não dá para fazer essa diferença')
elif n == 3:
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    p = n1 * n2
    print(f'O produto ente {n1:.2f} e {n2:.2f} é: {p:.2f}')
elif n == 4:
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    d = n1 / n2
    if n2 == 0:
        print('Divisão por zero')
    else:
        print(f'A divisão entre {n1:.2f} e {n2:.2f} é: {d:.2f}')
else:
    print('Opção não encontrada, escolha um número entre 1 e 4')