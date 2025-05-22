from random import randint
alunomes = {}

for i in range(5):
    nome = str(input("Digite o nome do aluno: "))
    notas = []
    est = {}
    for i2 in range(4):
        n = randint(1, 10)
        notas.append(n)
    alunomes[nome] = notas
    media = sum(notas)/4
    est['notas'] = notas
    est['media'] = media
    alunomes[nome] = est
print(alunomes.items())
# tuplas são as unicas que podemos usar nesse caso acima, por conta da sua imutabilidade. Listas deram erro por serem mutáveis
while True:
    decision = (input("Digite o que deseja procurar (0 para sair)\n> "))
    if decision == "0":
        break
    else:
        if alunomes.get(decision):
            print(alunomes[decision])
