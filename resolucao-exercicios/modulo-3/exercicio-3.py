from random import randint

numero_randomico = randint(1,25)

num_palpites = 5;
jogar_novamente = "s"

while jogar_novamente == "s":
    while num_palpites > 0:
        palpite = int(input("Digite seu palpite: "))
        if palpite == numero_randomico:
            print("Você acertou!")
            break;
        elif palpite > numero_randomico:
            print("O seu palpite é maior que o número")
        else: 
            print("O seu palpite é menor que o número")
        num_palpites -= 1
    if (num_palpites == 0):
        print("Seus palpites acabaram. Você perdeu!")
    
    jogar_novamente = input("Deseja jogar novamente?[s/n] ")
    if jogar_novamente == "s":
        num_palpites = 5
        numero_randomico = randint(1, 25)

    
