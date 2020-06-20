from random import choice

computador = choice(['pedra', 'papel', 'tesoura'])
empate = "Temos um empate!"
venceu = "Você venceu!"
perdeu = "Você perdeu!"
print("---- Pedra, Papel e Tesoura ----")
jogador = input("Sua jogada: ")
if jogador != "pedra" and jogador != "papel" and jogador != "tesoura":
    print("Você precisa inserir uma jogada válida!")
else:
    print(f"O computador jogou: {computador}")
    if jogador == "pedra":
        if computador == "pedra":
            print(empate)
        elif computador == "tesoura":
            print(venceu)
        else:
            print(perdeu)
    elif jogador == "papel":
        if computador == "pedra":
            print(venceu)
        elif computador == "papel":
            print(empate)
        else:
            print(perdeu)
    else: # jogador escolheu tesoura 
        if computador == "pedra":
            print(perdeu) 
        elif computador == "papel":
            print(venceu)
        else:
            print(empate)
