import math
print('Digite a altura do degraus de uma escada e a altura que ele quer chegar, mostrará quantos degraus'
      ' precisa subir para atingir o seu objetivo')
degraus = float(input())
altura_desejada = float(input())
total =math.ceil(altura_desejada / degraus)
print(f'Precisará subir: {total} degraus')