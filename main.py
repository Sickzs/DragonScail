from jogo.campanha import *
from jogo.jogador import *
from jogo.enemy import *
from jogo.events import *

import os


def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.getenv("TERM"):
        os.system("clear")
    else:
        print("\n" * 50)

try:
    menu = """
╔════════════════════════════╗
║        DRAGONSCAIL         ║
╚════════════════════════════╝

[ 1 ] Solo
[ 2 ] Multiplayer Online
[ 3 ] Multiplayer local
[ 4 ] multiplayer LAN
[ 5 ] configurações
[ 6 ] Carregar Jogo
[ 0 ] Sair 
"""

    clear()
    print(menu)

    selecione = int(
        input("Digite um numero e selecione uma opção: ")
    )

    if selecione == 1:
        clear()

        menu_classe = """
╔════════════════════════════╗
║        DRAGONSCAIL         ║
╚════════════════════════════╝

[ 1 ] Guerreiro
[ 2 ] Mago 
[ 3 ] Solo
"""

        print(menu_classe)

        selecione = int(input("Escolha uma classe: "))

        if selecione == 1:
            name = str(
                input("Digite o nome do personagem: ")
            )
            player = Guerreiro(name, 150, 150)
            iniciar_campanha(player)
        elif selecione == 2:
            name = str(
                input("Digite o nome do personagem: "))
            player = Mago(name, 100, 100)
            iniciar_campanha(player)
        elif selecione == 3:
            name = str(
                input("Digite o nome do personagem: ")
            )

            player = Solo(name, 125, 125)

            iniciar_campanha(player)

    elif selecione == 2:
        print(" [!] Opção ainda indisponivel ")

    elif selecione == 3:
        print(" [!] Opção ainda indisponivel")

    elif selecione == 4:
        print(" [!] Opção ainda indisponivel")

    elif selecione == 5:
        print(" [!]Opção ainda indisponivel")

    elif selecione == 6:
        print(" [!] Opção ainda indisponivel")

    elif selecione == 0:
        print(" [!] Saindo do Jogo ")
        exit()


except KeyboardInterrupt:
    print("[!] Parando o jogo.")
    exit()

except ValueError:
    print("[!] Digite apenas numeros inteiros.")
    exit()