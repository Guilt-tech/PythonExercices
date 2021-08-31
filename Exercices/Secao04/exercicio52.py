print('Digite os valores das três apostas e o valor total do prêmio, que será dividido proporcionalmente ao preço apostado por cada um')
ap1 = float(input('Preço apostado: '))
ap2 = float(input('Preço apostado: '))
ap3 = float(input('Preço apostado: '))
premio = int(input('Valor do prêmio: '))
Total = ap1 + ap2 + ap3
v1 = ap1 / Total
v2 = ap2 / Total
v3 = ap3 / Total
val1 = v1 * premio
val2 = v2 * premio
val3 = v3 * premio
print(f"O premio do apostador 1 é: {val1:.2f}")
print(f"O premio do apostador 2 é: {val2:.2f}")
print(f"O premio do apostador 3 é: {val3:.2f}")