import random

def jogar():
    exibeCabecalho()
    palavra_secreta = arquivoPalavraSecreta()

    acertos = inicializaMascara(palavra_secreta)
    print(acertos)

    enforcou = False
    acertou = False
    errou = 0

    while(not enforcou and not acertou):
        chute = Palpitar()

        if(chute in palavra_secreta):
            posicionaChuteCerto(acertos, chute, palavra_secreta)
        else:
            errou += 1
            desenha_forca(errou)

        enforcou = (errou == 7)
        acertou = ('_' not in acertos)
        print(acertos)

    if(acertou):
        msgVenceu()
    else:
        msgPerdeu(palavra_secreta)



def posicionaChuteCerto(acertos, chute, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if (chute == letra):
            acertos[i] = letra
        i += 1


def Palpitar():
    chute = input("Qual letra: ")
    chute = chute.strip().upper()
    return chute


def inicializaMascara(palavra_secreta):
    return ['_' for letra in palavra_secreta]


def arquivoPalavraSecreta():
    arquivo = open("Frutas.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def exibeCabecalho():
    print("******************")
    print("Well come to game.")
    print("******************")


def msgVenceu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def msgPerdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar()
