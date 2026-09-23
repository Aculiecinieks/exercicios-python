lista = [3, 7, 12, 5, 9]
maior = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero

print(f"Maior valor: {maior}")
