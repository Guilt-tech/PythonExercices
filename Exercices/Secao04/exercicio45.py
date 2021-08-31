print('Digite uma letra maiúscula para ser convertida em letra minúscula')
maiuscula = input('Letra maiúscula: ')
ordena_AscII_maiuscula = ord(maiuscula)
ordena_AscII_minuscula = ord(maiuscula) + 32
minuscula = chr(ordena_AscII_minuscula)
print(f'A letra em minúsculo é: {minuscula} e em maisculo é: {maiuscula}')
