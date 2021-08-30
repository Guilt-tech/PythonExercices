print('Digite o valor da hora de trabalho (em reais) e o número de horas trabalhadas por mês, '
      'irá fazer o valor o cálculo do salário do funcionário com um acréscimo de 10%' )
hora_de_trabalho = float(input())
horas_trabalhadas = float(input())
salario = horas_trabalhadas * hora_de_trabalho
salario_acrescido = salario * (10 / 100)
total = salario + salario_acrescido
print(f'O salrio do funcionário com um acréscimo de 10% é: R${total:.2f}')