
total = 0

for i in range(5):
    numero = int(input("Digite o numero que deseja adicionar a soma: "))
    pergu = input ("deseja incluir ele no total?")

    if pergu == "s":
        total += numero
        
print('o total dos numeros adicionado deu: {}'.format(total))


print('Gabriel bartholdy')