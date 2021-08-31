print('Digite o salário e o valor da prestação de um empréstimo')
s = float(input('Salário: '))
e = float(input('Empréstimo: '))
prest = s * (20 / 100)
emp = s + prest
if emp > e:
    print(f'Empréstimo não concedidio')
else:
    print(f'Empréstimo concedido')