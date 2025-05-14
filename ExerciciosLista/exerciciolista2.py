import random
nomes_candidatos = [
    "Kenzo", "Robert", "Thompson", "Nulo/Branco"
]
votos = [0, 0, 0, 0]
for i in range(1000):
    votos[random.randint(0, 3)] += 1
nova_lista = list(zip(nomes_candidatos, votos))
print(f"Candidatos e seus votos: {nova_lista}\nCandidato com maior voto: {nova_lista[votos.index(max(votos))]}\nQuantidade de votos Nulos:{votos[3]}")
for i in range(4):
    print(f"{nomes_candidatos[i]}: {votos[i] / 1000 * 100:.2f}% de votos")