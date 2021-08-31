print('Digite um número entre 1 e 12, para ver o mês')
Mes = ['1-Janeiro', '2-Fevereiro', '3-Março', '4-Abril', '5-Maio', '6-Junho', '7-Julho', '8-Agosto', '9-Setembro', '10-Outubro', '11-Novembro', '12-Dezembro']
mes = int(input('Número: '))
if 1 < mes > 12:
    print('Mês inválido')
else:
    print(f'O mês é: {Mes[mes - 1]}')