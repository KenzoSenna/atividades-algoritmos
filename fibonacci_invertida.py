a = 0
b = 1
lista = "0, 1"
qeue_number = int(input("Digite até que número da sequência de Fibonacci voce quer percorrer?\n: "))
for counter in range(qeue_number - 2):
    c = a + b
    lista = lista + ","+" " + str(c)
    print(f"sequencia = {lista}")
    a = b
    b = c
print("Sequência de fibonacci reversa: ", lista[::-1])