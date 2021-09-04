print('Digite as respostas das somas')
import  random
count = 0
acertos = 0
while count < 5:
    count = count + 1
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    resp = int(input(f'Digite a soma de {num1} + {num2}: '))
    Resp = num1 + num2
    if resp != Resp:
        print(f'Você errou a soma entre {num1} e {num2}, a resposta certa é: {Resp}')
        print(f'Você tem {acertos} acertos')
    else:
        print(f'Você acertou a soma entre {num1} e {num2}, a resposta certa é: {Resp}')
        acertos = acertos + 1
        print(f'Você tem {acertos} acertos')
        