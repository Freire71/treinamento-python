intervalo_inicial = int(input("Digite o valor inicial do intervalo: "))
intervalo_final = int(input("Digite o valor final do intervalo (não incluso): "))

intervalo = range(intervalo_inicial, intervalo_final)

acumulador = 0
for numero in intervalo:
    if numero % 2 == 1:
        print(numero)
    else:
        acumulador += numero
    
print(f"Valor final do acumulador: {acumulador}")