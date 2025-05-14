qnt_termos = int(input("Quantos termos da série você quer somar? "))
soma = 0
for i in range(1, qnt_termos + 1):
    if i % 2 != 0:
        soma += 1 / i
        print(f"+ 1 / {i}")
    else:
        soma -= 1 / i
        print(f"- 1 / {i}")
print(f"A soma dos {qnt_termos} primeiros termos da série harmônica alternada é: {soma}")
