nomes = ["Tony Stark", "Peter Parker", "Thor"]

nomes_2 = [ nome[0].lower() for nome in nomes ]
nomes_3 = []
for nome in nomes:
    nomes_3.append(nomes[0].lower())

print(nomes_2)
print(nomes_3)

numeros = [1, 2, 3, 4, 5, 6]
print("XD")
numeros_2 = [num for num in numeros if num % 2 == 1 ]
numeros_3 = []

for num in numeros:
    if num % 2 == 1: 
        numeros_3.append(num)

print(numeros_2)
print(numeros_3)
