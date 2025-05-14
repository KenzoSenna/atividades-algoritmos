
quantity_interval = int(input("Digite o intervalo que deseja: "))
if quantity_interval > 1:
    for counter in range(2, quantity_interval+1):
        number = counter
        numPrimo = 0
        for i in range(1, (number + 1)):
            if number % i == 0:
                numPrimo += 1
                
        if numPrimo == 2:
            print(counter, ' primo | ', end='')
        else:
            print(counter, ' não primo | ', end='')

elif quantity_interval == 0:
    print(quantity_interval, '0 números de intervalo? é sério?')