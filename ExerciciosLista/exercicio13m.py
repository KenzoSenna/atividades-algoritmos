numeros = []
decision = 1; soma = 0
while decision != -1:
    decision = float(input("Digite o número que deseja\nDigite (-1) para sair\n: "))
    if decision != -1:
        numeros.append(decision)
for num in numeros:
    soma += num
if len(numeros) != 0:
    print(soma / len(numeros))