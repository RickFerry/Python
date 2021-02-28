import Adivinhacao
import forca


def escolherJogo():
    print("******************")
    print("Choose youre game.")
    print("******************")

    escolha = int(input("1)Adivinhação\n2)Forca\nQual você quer jogar: "))

    if (escolha == 1):
        Adivinhacao.jogar()
    elif (escolha == 2):
        forca.jogar()
    else:
        print("")


if (__name__ == "__main__"):
    escolherJogo()
