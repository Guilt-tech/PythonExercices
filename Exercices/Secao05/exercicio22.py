print('Digite a idadde e o tempo de serviço, para podeer saber se pode ou não se aposentar')
idade = int(input("Idade: "))
tempo_servico = int(input('Tempo de serviço: '))
if idade >= 65 or tempo_servico >= 30 or idade >= 60 and tempo_servico >= 25:
    print("Pode se aposentar")
else:
    print('Não pode se aposentar')