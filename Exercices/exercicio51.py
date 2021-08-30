print('Digite as coordenadas x e y, que irá calcular a sua distância da origem')
x = float(input())
y = float(input())
distancia = int((((0 - x) ** 2) + ((0 - y) ** 2)) ** (1 / 2))
print(f'A distância entre a origem (0,0) e o ponto de'
      f' coordenadas ({x},{y})é: {distancia}')