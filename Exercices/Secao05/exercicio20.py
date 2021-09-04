print('Digite três valores, para ver se é um trinângulo, e se forem se é um triânguulo escaleno, equilátero ou isóceles')
A = float(input('Lado A: '))
B = float(input('Lado B: '))
C = float(input('Lado C: '))
soma = A + B
soma1 = A + C
soma2 = B + C
if A and B and C < soma and soma1 and soma2:
    if A == B == C:
        print('Triângulo Equilátero')
    if A == B != C or A == C != B or B == C != A:
        print('Triângulo isóceles')
    if A != B and A != C and B != C:
        print('Triângulo escaleno')
else:
    print('Não formam um triângulo')