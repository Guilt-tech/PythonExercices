import math
print('Digite um número, para ver se ele é positivo ou negativo, se for positivo calcula a raiz quadrada e se for negativo o número irá ser inválido')
n = int(input('Número: '))
if n > 0:
    raiz = math.sqrt(n)
    print(f'A raíz quadrado de {n} é: {raiz}')
else:
    print('Número inválido, digite um número positivo')