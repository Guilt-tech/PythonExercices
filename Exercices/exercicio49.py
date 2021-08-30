print('Digite o horário (hora, minuto(s) e segundo(s)) e qual foi a duração em segundos')
hora = int(input())
min = int(input())
seg = int(input())
duracao_seg = int(input())
hora = hora * 3600
min = min * 600
totalSegundos = hora + min + seg + duracao_seg
horaFinal = int(totalSegundos / 3600)
resultado = totalSegundos % 3600
minFinal = int(resultado / 60)
resultado = resultado % 60
print(f'A experiência irá terminar as: {horaFinal}:{minFinal}:{resultado}')