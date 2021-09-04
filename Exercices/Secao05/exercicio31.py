print('Digite a altura e o peso de uma, para ver qual a classe ela pertence')
alt = float(input('Altura: '))
peso = float(input('Peso: '))
if alt < 1.20:
    if peso < 61:
        print('Você pertence a classe A')
    elif  60 < peso < 90:
        print('Você pertence a classe D')
    else:
        print('Você pertence a classe G')
elif 1.71 > alt > 1.19:
    if peso < 61:
        print('Você pertence a classe B')
    elif  60 < peso < 90:
        print('Você pertence a classe E')
    else:
        print('Você pertence a classe H')   
else:
    if peso < 61:
        print('Você pertence a classe C')
    elif  60 < peso < 90:
        print('Você pertence a classe F')
    else:
        print('Você pertence a classe I')