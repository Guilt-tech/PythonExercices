print('Digite a sua idade e o ano atual, para calcular o ano de nascimento')
idade = int(input('Idade: '))
ano = int(input('Ano: '))
ano_nascimento = ano - idade
print(f'A pessoa nasceu em: {ano_nascimento}')