print('Digite 3 números e 1-4, para escolher as médias que serão calculadas')
print('1- Geométrica \n'
        '2- Ponderada \n'
        '3- Harmônica \n'
        '4- Aritmética \n')
media = int(input('Média: '))
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
if media == 1:
    geo = (n1 * n2 * n3) ** (1/3)
    print(f'A média geométrica de: {n1:.2f}, {n2:.2f} e {n3:.2f} é: {geo:.2f}')
elif media == 2:
    pond = (n1 + 2 * n2 + 3 * n3) / 6
    print(f'A média ponderada de: {n1:.2f}, {n2:.2f} e {n3:.2f} é: {pond:.2f}')
elif media == 3:
    har = 1 / ((1 / n1) + (1 / n2) + (1 / n3))
    print(f'A média harmônica de: {n1:.2f}, {n2:.2f} e {n3:.2f} é: {har:.2f}')
else:
    ari = (n1 + n2 + n3) / 3
    print(f'A média aritmética de: {n1:.2f}, {n2:.2f} e {n3:.2f} é: {ari:.2f}')