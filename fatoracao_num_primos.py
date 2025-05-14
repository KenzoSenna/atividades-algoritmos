listaPrimos = []
listaPrimosFatorados = []
quantity_interval = int(input("Digite o intervalo que deseja: "))
if quantity_interval > 1:
    for counter in range(2, quantity_interval+1):
        number = counter
        numPrimo = 0
        for i in range(1, (number + 1)):
            if number % i == 0:
                numPrimo += 1
        if numPrimo == 2:
            listaPrimos.append(number)
        for numeros in listaPrimos:
            menorNum = min(listaPrimos)
            posicao = listaPrimos.index(menorNum)
            while quantity_interval % menorNum == 0:
                listaPrimosFatorados.append(menorNum)
                quantity_interval /= menorNum
                print(listaPrimosFatorados)
            listaPrimos.pop(posicao)
            if quantity_interval == 1:
                break
elif quantity_interval == 0:
    print(quantity_interval, '0 números de intervalo? é sério?')