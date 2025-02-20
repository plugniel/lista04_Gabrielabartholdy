horario_disp = []
n = int(input('Quantos horarios deseja adicionar na lista?'))

for i in range(n):
    horario = input('Digite o horario')
    horario_disp.append(horario)
for i in range(len(horario_disp)):
    print('\nHorarios disponiveis:')
    for i,horario in  enumerate(horario_disp):
        print("{}°{}".format(i+1,horario))
    escolha_h = int(input("escolha o horario pelo numero"))
    if 1 <= escolha_h <= len(horario_disp):
        hora_sele = horario_disp[escolha_h - 1]
        print("Horario de {} foi agendado com sucesso".format(hora_sele))
        horario_disp.remove(hora_sele)
    else:
        print("Valor invalido")
    if len(hora_sele) == 0:
        print("Todos os horarios marcados")
        break
    conti = input("deseja marcar mais um horario?(s,n)")
    if conti != 's':
        print("encerrando...")
        break
    
