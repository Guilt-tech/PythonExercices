print('D|igite a altura e o sexo (1 para homem e 2 para mulher) de uma pessoa')
h = float(input('Altura: '))
s = int(input('Sexo: '))
if s == 1:
    homem = (72.7 * h) - 58
    print(f'O seu peso ideal é: {homem:.2f}')
elif s == 2:
    mulher = (63.1 * h) - 44.7
    print(f'O seu peso ideal é: {mulher:.2f}')
else:
    print('Você não digitou um código para o sexo')