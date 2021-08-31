print('Digite um número inteiro, para ver se ele é divisível por 3 ou por 5, mas não os dois respectivamente')
num = int(input('Número 1: '))
if num % 3 == 0 and num % 5 == 0:
    print('Não pode ser divisível pelos dois ao mesmo tempo')
elif num % 3 == 0:
    print(f'O número {num} é divisível por 3')
else:
    num % 5 == 0
    print(f'O número {num} é divisível por 5')