from rich import print, status
from abc import ABC, abstractmethod
from jogo.enemy import *
from jogo.jogador import *

import pandas
import json
import os
import random
import time
import socket
import threading






def iniciar_campanha(player):
    print("Vila de Pedra Clara\n")
    time.sleep(3)

    print(
        "\nDepois de horas caminhando por uma estrada cercada "
        "por florestas densas, você finalmente avista pequenas "
        "colunas de fumaça subindo atrás das colinas.\n"
    )

    time.sleep(15)

    print(
        "Ao atravessar uma velha ponte de madeira, surge "
        "diante de você a Vila de Pedra Clara.\n"
    )

    time.sleep(5)

    print(
        "Casas simples de madeira e pedra estão espalhadas "
        "ao redor de uma pequena praça. Camponeses carregam "
        "sacos de grãos, crianças correm entre as construções "
        "e o som do martelo de um ferreiro ecoa por toda a vila.\n"
    )

    time.sleep(15)

    print("À primeira vista, tudo parece tranquilo.\n")
    time.sleep(3)

    print("Porém, algo está errado.\n")
    time.sleep(3)

    print(
        "Os moradores evitam olhar para a floresta. Algumas "
        "casas possuem marcas profundas nas portas, como se "
        "alguma criatura tivesse tentado entrar durante a noite. "
        "Próximo ao poço central, um quadro de avisos exibe "
        "vários pedidos de ajuda.\n"
    )

    time.sleep(15)

    print("Entre eles, um aviso chama sua atenção: \n")
    time.sleep(3)

    print(
        "> **“Recompensa para quem encontrar os moradores "
        "desaparecidos na Floresta Sombria. Falar com o chefe "
        "da vila.”**\n"
    )

    time.sleep(5)

    print(
        "Enquanto você observa o aviso, um velho se "
        "aproxima lentamente.\n"
    )

    time.sleep(4.5)

    print(
        "— Você não parece ser daqui — diz ele, apoiando-se "
        "em um cajado. — Se está procurando trabalho, chegou "
        "em uma boa hora. Pedra Clara precisa de alguém "
        "corajoso… ou louco o bastante para entrar naquela "
        "floresta.\n"
    )

    time.sleep(15)

    print("Sua jornada realmente começa agora.\n")
    time.sleep(5)

    menu_missao = """
╔════════════════════════════╗
║          MISSÃO            ║
╚════════════════════════════╝

[ 1 ] Aceitar missão
[ 2 ] Negar missão
[ 0 ] Sair
"""

    print(menu_missao)

    selecione = int(input("Escolha uma opção: "))

    if selecione == 1:
        print(" [!] Missão Aceita")

        menu_pos_missao = """
╔════════════════════════════╗
║         DRAGONSCAIL        ║
╚════════════════════════════╝

[ 1 ] Ir até A floresta sombria
[ 2 ] Ficar e treinar
[ 3 ] Ir conseguir mais informações
[ 0 ] Sair
"""

        print(menu_pos_missao)

        selecione = int(input("Escolha uma opção: "))

        if selecione == 1:
            print(" [+] Caminhando até a floresta sombria...")
            time.sleep(120)

            batalha = """
╔════════════════════════════╗
║           BATALHA          ║
╚════════════════════════════╝
[ 1 ] Atacar
[ 2 ] Status
[ 3 ] Inventário
[ 0 ] Fugir
"""
            print(batalha)
            selecione = int(input("\nDigite um numero: "))
            if selecione == 2:
                player.status()
                input("\nClique Enter Para retornar a batalha")
            elif selecione == 3:
                print("[!] Opção Indisponivel ainda")
            elif selecione == 0:
                run = random.choices([0, 1])
                weights=90, 10
                k=1
                if run == 0:
                   return print(f"[!] Você não conseguiu fugir")
                elif run == 1:
                    print(f"[+] Você conseguiu Fugir!")
                    exit()

            elif selecione == 1:
                goblin = Goblin("Goblin", 100, 100)

                if selecione == 1:
                    target = int(input("""
╔════════════════════════════╗
║            ALVO            ║
╚════════════════════════════╝                

[ 1 ] Goblin

Digite uma opção: """))
                    while player.life > 0 and goblin.life > 0:
                        if target == 1:
                            player.send_damage(goblin, 50)
                            goblin.send_damage(player, 50)

                            if goblin.life > 0 and player.life > 0:
                                print(batalha)

                                selecione = int(
                                    input("\nDigite um numero: ")
                                )

                                if selecione == 1:
                                    target = int(input("""
╔════════════════════════════╗
║            ALVO            ║                                
╚════════════════════════════╝                

[ 1 ] Goblin
                                    
Digite uma opção: """))
                            elif goblin.life > 0 and player.life <= 0:
                                print("[-] Você morreu!")
                                exit(0)
                            elif goblin.life <= 0 and player.life > 0:
                                print("[+] Parabéns, Você matou o goblin!")
                                print("[+] Item ganho: Adaga de goblin")
                                print("[+] +20 XP ")
                            else:
                                print("[!] Alvo inválido.")

                            break
    elif selecione == 2:
        print(" [!] Missão Negada")
        exit()

    elif selecione == 0:
        print(" [!] Saindo do Jogo")
        exit()