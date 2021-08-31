print('Digite três notas do aluno, para calcular a sua média ponderada')
n1 =float(input('Nota 1: '))
n2 =float(input('Nota 2: '))
n3 =float(input('Nota 3: '))
media_ponderada = ((n1 * 1) + (n2 * 1) + (n3 * 2)) / (1 + 1 + 2)
print(f'A media do aluno foi: {media_ponderada}')
if media_ponderada >= 6:
    print("Aprovado")
else:
    print('Reprovado')