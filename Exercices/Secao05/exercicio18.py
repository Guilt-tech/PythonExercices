print('Digite 1, 2, 3 ou 4, para escolher qual operação:')
print(['1-Soma', '2-Subtração', '3-Multiplicação', '4-Divisão'])
num = int(input('Número: '))
print('Agora digite dois valores para essa operação')
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
if num == 1:
    soma = num1 + num2
    print(f'A soma de: {num1:.2f} '+' {num2:.2f}  é: {soma:.2f}')
elif num == 2:
    subtracao = num1 - num2
    print(f'A subtração de: {num1:.2f} '-' {num2:.2f}  é: {subtracao:.2f}')
elif num == 3:
    multiplicacao = num1 * num2
    print(f'A multiplicação de: {num1:.2f} '*' {num2:.2f}  é: {multiplicacao:.2f}')
else:
    divisao = num1 / num2
    print(f'A divisão de: {num1:.2f} '/' {num2:.2f}  é: {divisao:.2f}')