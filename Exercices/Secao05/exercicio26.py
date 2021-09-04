print('Digite a distância em Km e a quantidade de litros de gasolina consumidos, para calcular o consumo em km/l')
km = float(input('km: '))
l = float(input('litros: '))
consumo = km / l
if consumo < 8:
    print('Venda o carro!')
elif 7 < consumo <12:
    print('Econômico!')
elif consumo > 12:
    print('Super econômico!')