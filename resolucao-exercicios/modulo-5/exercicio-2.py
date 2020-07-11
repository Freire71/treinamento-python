# Dada a lista de filantropos abaixo,
# Itere sobre todos eles para calcular o total doado e imprima ao final esse valor
# Também guarde o nome e o valor da maior doação realizada por um único filantropo
# Imprima ao final quem foi o maior o doado e qual foi o valor doado


filantropos = [
    {"nome": "Bill e Melinda Gates", "total_doado": "R$ 117 bi"},
    {"nome": "Warren Buffett", "total_doado": "R$ 82 bi"},
    {"nome": "George Soros", "total_doado": "R$ 31 bi"},
    {"nome": "Azim Premji", "total_doado": "R$ 31 bi"},
]

maior_filantropo = {}
maior_doacao = 0
total_doado = 0
for filantropo in filantropos:
  print(filantropo)
  doacao = filantropo["total_doado"].split(" ")
  valor = float(doacao[1])
  total_doado += valor

  if valor > maior_doacao:
    maior_doacao = valor
    maior_filantropo =  filantropo
    
print(f"Total doado {total_doado}")
print(f"O maior doador foi {maior_filantropo['nome']} com uma quantia de {maior_filantropo['total_doado']}")
  
