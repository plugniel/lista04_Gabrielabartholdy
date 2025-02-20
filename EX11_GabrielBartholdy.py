tarefas = int (input('Quantas tarefa deseja realizar?'))
tare = []
conclu = []

for i in range(tarefas):
        ss = input("Qual o nome da tarefa?")
        tare.append(ss)
        print("")
        ss1 = input("Esta tarefa esta concluida?")
        conclu.append(ss1)
        print('')
        print( "TAREFA:{} \nCONCLUIDA:{}".format(tare[i],conclu[i]))


print('Gabriel bartholdy')