dire = input("Qual a direção que deseja apontar?(C para cima, A para baixo) ")

if dire == 'a':
    num = int(input("qual o numero que deseja? (Abaixo de 20)"))
    for i in range(20,num ,-1):
        print(i)
elif dire == 'c':
    num = int(input("qual o numero que deseja? (Superior a 1)"))
    for i in range(num):
        print(i)
