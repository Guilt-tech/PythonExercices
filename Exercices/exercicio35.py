import math
print('Digite os valores dos catetos a e b, para saber qual é a hipotenusa')
a = float(input())
b = float(input())
hipotenusa = math.sqrt(a ** 2 + b ** 2)
print(f'O resultado da hipotenusa com os catetos {a} e {b} é: {hipotenusa}')