print('Digite a idade de um nadador, para classifica-lo em uma das categorias')
idade = int(input('Idade: '))
if 5 <= idade <= 7:
    print('Categoria: Infatil A')
elif 8 <= idade <= 10:
    print('Categoria: Infantil B')
elif 11 <= idade <= 13:
    print('Categoria: Juvenil A')
elif 14 <= idade <=17:
    print('Categoria: Juvenil B')
else:
    print('Categoria: Sênnior')