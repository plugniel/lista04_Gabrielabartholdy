numero = int(input("Digite o número para ver a contagem regressiva: "))

if numero < 50: 
    for i in range(50,numero ,-1):
        print(i)
else:
    print('o numero deve ser menor que 50')


print('Gabriel bartholdy')