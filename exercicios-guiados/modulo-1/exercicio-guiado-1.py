#### Álcool ou Gasolina? ##### 

# Requisitando entrada de dados
valor_gasolina_str = input("Digite o valor da gasolina: ")
valor_alcool_str = input("Digite o valor do álcool: ")

# Realizando a conversão dos valores
valor_gasolina = float(valor_gasolina_str)
valor_alcool = float(valor_alcool_str)

# Calculando e imprimindo o valor formatado com 3 casas decimais
alcool_por_gasolina = valor_alcool/valor_gasolina
print(f"Proporção: {alcool_por_gasolina:.3f}")

# Condicional chave do nosso programa
if alcool_por_gasolina >= 0.70:
  print("É melhor abastecer com gasolina!")
else: 
  print("É melhor abastecer com álcool!")
