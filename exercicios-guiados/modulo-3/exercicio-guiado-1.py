# CENSO 

# Qual a média do salário da população?
# Qual a média de filhos?
# Qual a maior quantidade de filhos em uma familia?
# Qual o maior salário? 
# Qual o percentual de pessoas que ganham até um salário minimo?

maior_salario = 0.0
maior_numero_de_filhos = 0

salarios = []
numero_de_filhos = []

numero_de_participantes = int(input("Digite o número de pessoas que participarão da pesquisa: "))

indice = 0

while indice < numero_de_participantes:
    filhos = int(input("Número de filhos:"))
    salario = float(input("Salário: "))
    
    numero_de_filhos.append(filhos)
    salarios.append(salario)
    if filhos > maior_numero_de_filhos:
        maior_numero_de_filhos = filhos
    if salario > maior_salario:
        maior_salario = salario
    indice += 1

media_filhos = 0
for filhos in numero_de_filhos:
    media_filhos += filhos

media_filhos = media_filhos/len(numero_de_filhos)

media_salarios = 0
salarios_minimo = 0
for salario in salarios:
    media_salarios += salario
    if salario <= 1045:
        salarios_minimo += 1
media_salarios = media_salarios/len(salarios)

porcentagem_salarios_minimos = (salarios_minimo/len(salarios)) * 100


print("----------- Pesquisa Concluída -----------")
print(f"Média dos salários: R${media_salarios:.2f}")
print(f"Média de filhos: {media_filhos}")
print(f"Maior quantidade de filhos em uma família: {maior_numero_de_filhos}")
print(f"O maior salário é de: R${maior_salario:.2f}")
print(f"O percentual de pessoas que ganham até um salário {porcentagem_salarios_minimos:.2f}%")


