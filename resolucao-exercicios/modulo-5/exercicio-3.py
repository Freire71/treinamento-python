# Dada a lista de artistas abaixo
# Itere sobre todos os eles, imprimindo o nome completo e a idade de cada um (de forma aproximada)

from datetime import date

data_hoje = date.today()

artistas = [
    {"nome": "Dua", "sobrenome": "Lipa", "data_nascimento": "22/08/1995"},
    {"nome": "Ashley", "sobrenome": "Frangipane", "data_nascimento": "29/09/1994"},
    {"nome": "Adam", "sobrenome": "Levine", "data_nascimento": "18/03/1979"},
    {"nome": "Justin", "sobrenome": "Timberlake", "data_nascimento": "31/03/1981"},
]

for artista in artistas:
  nome_completo = f"{artista['nome']} {artista['sobrenome']}" 
  data_separada = artista["data_nascimento"].split("/")
  ano = int(data_separada[2])
  idade = data_hoje.year - ano
  print(f"Nome: {nome_completo} - Idade: {idade} anos")
