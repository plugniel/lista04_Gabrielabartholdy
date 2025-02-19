
total = 0

for i in range(5):
    numero = int(input("Digite o numero: "))
    pergu = input ("deseja incluir ele no total?")

    if pergu == "s":
        total += numero
        
print('o total dos numeros adicionado deu: {}'.format(total))