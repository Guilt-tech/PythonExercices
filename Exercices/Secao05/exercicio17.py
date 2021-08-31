print('Digite tres números, para calcular a area do trapezio')
baseMaior = float(input('Base maior: '))
baseMenor = float(input('Base menor: '))
altura = float(input('Altura: '))
area = ((baseMaior + baseMenor) * altura) / 2
if baseMaior > 0 and baseMenor > 0:
    print(f'A area do trapezio é: {area}')
else:
    print('Números Inválidos')