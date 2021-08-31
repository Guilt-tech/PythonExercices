import math
print('Digite um número, para ver se é positivo ou negativo, se for positivo calcula a raiz quadrada e calcula ao quadrado e se for negativo o número vai ser inválido')
n = float(input('Número: '))
if n > 0:
    raiz = math.sqrt(n)
    print(f'A raíz quadrado de {n} é: {raiz}')
    quadrado = n ** 2
    print(f'O número ao quadrado de: {n} é: {quadrado}, digite um número positivo para calcular a sua raíz')
else:
    print('Número inválido, digite um número positivo')