import math
print('Digite um número real, para ver se é positivo ou negativo, se for positivo calcula a raiz quadrada e se for negativo calcula ao quadrado')
n = float(input('Número: '))
if n > 0:
    raiz = math.sqrt(n)
    print(f'A raíz quadrado de {n} é: {raiz}')
else:
    quadrado = n ** 2
    print(f'O número ao quadrado de: {n} é: {quadrado}, digite um número positivo para calcular a sua raíz')