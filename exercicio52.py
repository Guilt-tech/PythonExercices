print('Digite os valores das três apostas e o valor total do prêmio')
ap1 = float(input())
ap2 = float(input())
ap3 = float(input())
premio = int(input())
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