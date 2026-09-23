numero = int(input("Digite um numero: "))
fatorial = 1

for contador in range(1, numero + 1):
    fatorial *= contador

print(f"Fatorial de {numero}: {fatorial}")
