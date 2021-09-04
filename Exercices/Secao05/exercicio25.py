print('Digite os valores de a, b e c, para calcular as raízes da equação de 2° grau')
import math
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
delta = b ** 2 - 4 * a * c
if a != 0:
    if delta < 0:
        print('Não existe raiz')
    elif delta == 0:
        raizdelta = -1 * b + (math.sqrt(delta)) / (2 * a)
        print(f'A raiz é: {raizdelta:.2f} e é Raiz única')
    elif delta >= 0:
        raizdelta1 = -1 * b + (math.sqrt(delta)) / (2 * a)
        raizdelta2 = -1 * b - (math.sqrt(delta)) / (2 * a)
        print(f'As raizes são: {raizdelta1:.2f} e {raizdelta2:.2f}')
else:
    print('Não é uma equação de segundo grau')