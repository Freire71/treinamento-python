inteira = 30.0
meia = 15.0
filmes_em_cartaz = ["Vingadores - End Game", "Procurando Nemo", "Harry Potter e o cálice de Fogo" ] 
print("Seja bem vindo ao  CineSanar!")
print("Aqui vai a lista dos filmes em cartaz: ")

for indice, filme in enumerate(filmes_em_cartaz, start=1):
  print(f"{indice}) {filme}")

try: 
    opcao_digitada = int(input("Digite o número do filme que deseja assistir:"))
    filme_escolhido = filmes_em_cartaz[opcao_digitada - 1]
    print(f"Você escolheu o filme: {filme_escolhido}")
    
    possui_carteira = input("Possui carteira de estudante? [s/n]: ")
    if possui_carteira == "s":
        print(f"O valor total é R$ {meia}")
    else: 
        idade = int(input("Digite sua idade: "))
        if idade < 18 or idade >= 60:
            print(f"Você possui direito a meia-entrada. O valor total é R${meia}")
        else:
            print(f"Você não possui direito a meia-entrada. O valor total é R${inteira}")
except IndexError:
    print("Você digitou uma opção indisponível")
except ValueError:
    print("Você digitou um texto no lugar de um número")
