print('Digite um número inteiro positivo de três dígitos (100 a 999), para gerar o número invertido')
num = int(input('Número: '))
num = str(num)
reverso = num[::-1]
print(f'O número ao contrário de: {num} é: {reverso}')