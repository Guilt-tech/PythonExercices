print('Digite tres notas do aluno, para calcular a sua nota final')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)
print(f'A media do aluno foi: {media_ponderada}')
if 0 <= media_ponderada <= 2.9:
    print('Reprovado')
elif 3 >= media_ponderada <= 4.9:
    print('Recuperação')
else:
    print('Aprovado')