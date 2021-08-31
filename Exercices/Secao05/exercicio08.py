print('Digite duas notas de um aluno')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
if n1 >= 0 and n2 < 11 :
    media = (n1 + n2) / 2
    print(f'A média do aluno foi: {media}')
else:
    print(f'Nota inválida')