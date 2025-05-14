import random
numero = random.randint
sexos = "masculino", "feminino"
escolha = random.choice(sexos)
idade = random.randint(0, 100)
lista = [[0] * 3 for _ in range(5000)]
for listas in lista:
    listas[0] = numero
    listas[1] = idade
    listas[2] = escolha