pesoas = int (input('Quantas pessoas deseja convidar para a festa?'))
convi = []
if pesoas < 10:
    for i in range(pesoas):
        
        pes_conv = input("Qual o nome da pessoa que deseja convidar?")
        convi.append(pes_conv)
        print("pessoas convidadas:{} ".format(convi))
else:
    print("Numero muito alto")

print('Gabriel bartholdy')