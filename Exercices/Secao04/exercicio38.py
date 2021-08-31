print('Digite o salário de um funcionário e este irá receber um aumento de 25%')
salario = float(input('Salário: '))
aumento = salario * (25/100)
salario_com_aumento = salario + aumento
print(f'O novo salário do funcionário será: {salario_com_aumento} e o salario antigo era: {salario}')