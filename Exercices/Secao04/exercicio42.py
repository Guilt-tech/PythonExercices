print('Digite o salário-base do funcioário, que tem 5% de gratificação sobre o salário '
      'e que paga 7% de imposto sobre o salário')
salario_base = float(input('Salário Base: '))
gartificacao = salario_base * (5 / 100)
salario_gratificado = salario_base + gartificacao
imposto = salario_base * (7 / 100)
salario_imposto = salario_base - imposto
total = salario_gratificado - salario_imposto
total1 = salario_base + total
print(f'O salário do funcionário é: {total1:.2f}')