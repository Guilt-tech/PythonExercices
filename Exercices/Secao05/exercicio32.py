print('Digite o código do lanche e a quantidade, para calcular qual será o preço')
print('Especificação    Código    Preço \n'
    'Cachorro-Quente    100      1.20 \n'
    'Bauru Simples      101      1.30 \n'
    'Bauru com Ovo      102      1.50 \n'
    'Hamburguer         103      1.20 \n'
    'Cheeseburguer      104      1.70 \n' 
    'Suco               105      2.20 \n'
    'Refrigerante       106      1.00 \n')
Cod = str(input('Código: '))
Qtd = int(input('Quantidade: '))
comida = 'Cachorro Quente'
precoCQ = 1.20
comida1 = 'Bauru Simples'
precoBS = 1.30
comida2 = 'Bauru com ovo'
precoBO = 1.50
comida3 = 'Hamburguer'
precoH = 1.20
comida4 = 'Chesseburguer'
precoCb = 1.70
comida5 = 'Suco'
precoS = 2.20
comida6 = 'Refrigerante'
precoR = 1.00
if Cod == '100':
    pedido = Qtd * precoCQ
    print(f'O seu pedidio de {Qtd}x {comida} irá custar: R${pedido:.2f}')
elif Cod == '101':
    pedido1 = Qtd * precoBS
    print(f'O seu pedidio de {Qtd}x {comida} irá custar: R${pedido1:.2f}')
elif Cod == '102':
    pedido2 = Qtd * precoBO
    print(f'O seu pedidio de {Qtd}x {comida} irá custar: R${pedido2:.2f}')
elif Cod == '103':
    pedido3 = Qtd * precoH
    print(f'O seu pedidio de {Qtd}x {comida} irá custar: R${pedido3:.2f}')
elif Cod == '104':
    pedido4 = Qtd * precoCb
    print(f'O seu pedidio de {Qtd}x {comida} irá custar: R${pedido4:.2f}')
elif Cod == '105':
    pedido5 = Qtd * precoS
    print(f'O seu pedidio de {Qtd}x {comida} irá custar: R${pedido5:.2f}')
elif Cod == '106':
    pedido6 = Qtd * precoR
    print(f'O seu pedidio de {Qtd}x {comida} irá custar: R${pedido6:.2f}')