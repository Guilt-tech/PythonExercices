print('Digite um número entre 1 e 7, para ver o dia da semana')
diaSemana = ['1-Domingo', '2-Segunda-feira', '3-Terça-feira', '4-Quarta-feira', '5-Quinta-feira', '6-Sexta-feira', '7-Sábado']
dia = int(input('Número: '))
if 1 < dia < 7:
    print('Dia da semana inválido')
else:
    print(f'O dia da semana é: {diaSemana[dia - 1]}')