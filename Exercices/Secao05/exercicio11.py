print('Digite um número inteiro, para mostrar a soma de todos os seus algarismos, ex: 251 corresponderá ao valor 8 (2 + 5 + 1)')
n = int(input('Número: '))
n1 = str(n)
if n > 0:
    soma = int(n1[0]) + int(n1[1]) + int(n1[2])
    print(soma)
else:
    print('Número inválido')