import math
print('Digite um número inteiro, para ver o seu logarítmo')
n = int(input('Número: '))
if n < 0:
    print('Número inválido')
else:
    print(math.log(n))