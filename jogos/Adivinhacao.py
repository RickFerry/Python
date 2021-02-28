import random


def jogar():
    print("******************")
    print("Well come to game.")
    print("******************")

    # formatação de numeros com a função format
    # "{:7,2f}".format(3.99) numero flutuante com 7 casas antes da virgula e duas após...
    # "{:4d}".format(3) numero inteiro com 4 casas decimais...

    # numeroSecreto = round(random.random() * 100) Aleatorio entre 0.0 e 1.0 multiplicado por 100 e arendondado com'round'
    numeroSecreto = random.randrange(1, 101, 1)  # Aleatorio entre 1 e 100 e o intervalo
    tentativas = 0
    pontos = 1000
    i = 1

    print("1)Hard\n2)Normal\n3)Easy")
    escolha = int(input("Escolha o nivel do seu game: "))

    if (escolha == 1):
        tentativas = 5
    elif (escolha == 2):
        tentativas = 10
    elif (escolha == 3):
        tentativas = 20
    else:
        print("Por favor, escolha entre 1 e 3")

    # while(i <= 3):
    for i in range(1, tentativas + 1):
        print("Tentativa: {} de {} ".format(i, tentativas))
        chute = int(input("Seu palpite entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Por favor, numeros entre 1 e 100")
            continue

        if (chute == numeroSecreto):
            print("Você ganhou e fez {} pontos".format(pontos))
            break
        elif (chute > numeroSecreto):
            print("Você ultrapassou o numero correto, tente novamente.")
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = (pontos - pontosPerdidos)
        else:
            print("Sua tentativa foi menor que numero correto, tente novamente.")
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = (pontos - pontosPerdidos)
        # i = i + 1

    print("End Game...")


if (__name__ == "main"):
    jogar()
