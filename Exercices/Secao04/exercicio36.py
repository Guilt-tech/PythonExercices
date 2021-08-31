print('Digite a altura e o raio de um cilindro circular, para saber qual o seu volume')
raio = float(input('Raio: '))
altura = float(input('Altura: '))
pi = 3.141592
V = pi * (raio ** 2) * altura
print(f'O volume do cilindro com raio {raio} e altura {altura} é: {V}')