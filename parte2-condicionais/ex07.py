numero1 = int(input("Insira um numero: "))
numero2 = int(input("Insira um outro numero: "))

if numero1 < numero2:
    print(f"O {numero2} é maior")
elif numero1 > numero2:
    print(f"O {numero1} é maior")
else:
    print("Os dois sao iguais")