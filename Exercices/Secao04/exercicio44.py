import math
print('Digite a altura do degrau de uma escada e a altura que ele quer chegar, mostrará quantos degraus precisa subir para atingir o seu objetivo')
degraus = float(input('Altura do degrau: '))
altura_desejada = float(input('Altura que quer chegar: '))
total =math.ceil(altura_desejada / degraus)
print(f'Precisará subir: {total} degraus')