from abc import ABC, abstractmethod

from jogo import enemy
from jogo.enemy import Enemy, Goblin
from rich import *

import random


class jogador(ABC):
    def __init__(self, name, maxlife, life):
        self.name = name
        self.maxlife = maxlife
        self.life = life
        self.attacksmethods = []

    def receive_damage(self, damage):
        fator = random.randint(1, damage)
        self.life -= fator

        if self.life <= 0:
            self.life = 0

        print(
            f" [!] [blue]{self.name}[/] "
            f"Recebeu [red]dano de {fator}[/] "
        )

    def send_damage(self, target, strength=50):
        if self.life > 0 and target.life > 0:
            attack = self.attacksmethods[
                random.randrange(0, len(self.attacksmethods))
            ]

            print(
                f"[!] {self.name} atacou "
                f"{target.name} com um {attack}"
            )

            resultado = random.choice([0, 1])

            if resultado == 1:
                print(
                    f"[!] {self.name} Acertou um ataque "
                    f"contra {target.name}!"
                )

                target.receive_damage(strength)

            elif resultado == 0:
                print(
                    f"[!] {self.name} Errou um ataque "
                    f"contra {target.name}!"
                )

        else:
            print(
                f"[!] O ataque {self.name} -> "
                f"{target.name} não pode acontecer."
            )

    @abstractmethod
    def heartbeat(self):
        pass


class Guerreiro(jogador):
    def __init__(self, name, maxlife, life):
        super().__init__(name, maxlife, life)
        self.attacksmethods = ["Soco", "Chute"]

    def receive_damage(self, damage):
        fator = random.randint(1, damage)

        self.life -= fator

        if self.life <= 0:
            self.life = 0

        print(
            f" [!] [blue]{self.name}[/] "
            f"Recebeu [red]dano de {fator}[/] "
        )

    def send_damage(self, target, strength=50):
        if self.life > 0 and target.life > 0:
            attack = self.attacksmethods[
                random.randrange(0, len(self.attacksmethods))
            ]

            print(
                f"[!] {self.name} atacou "
                f"{target.name} com um {attack}"
            )

            resultado = random.choices(
                [0, 1],
                weights=[40, 60],
                k=1
            )[0]

            if resultado == 1:
                print(
                    f"[!] {self.name} Acertou um ataque "
                    f"contra {target.name}!"
                )

                target.receive_damage(strength)

            elif resultado == 0:
                print(
                    f"[!] {self.name} Errou um ataque "
                    f"contra {target.name}!"
                )

        else:
            print(
                f"[!] O ataque {self.name} -> "
                f"{target.name} não pode acontecer."
            )

    def heartbeat(self):
        pass

    def status(self):
        print(
            f"[red][!][/] [blue]{self.name}[/]"
            f"Vida: [green]{self.maxlife}:{self.life}[/]"
            f"Ataques: [red]{self.attacksmethods}[/]"
            
            f"[red][!] [Blue]{enemy.name}[/]"
            f"Vida Do Inimigo: [green]{enemy.life}:{enemy.maxlife}[/]"
        )
class Mago(jogador):
    def __init__(self, name, maxlife, life):
        super().__init__(name, maxlife, life)

        self.attacksmethods = [
            "Bola de fogo",
            "Raio de luz"
        ]

    def receive_damage(self, damage):
        pass

    def send_damage(self, target, strength=50):
        pass

    def heartbeat(self):
        pass

    def status(self):
        print(
            f"[red][!][/] [blue]{self.name}[/]"
            f"Vida: [green]{self.maxlife}:{self.life}[/]"
            f"Ataques: [red]{self.attacksmethods}[/]"

            f"[red][!] [Blue]{enemy.name}[/]"
            f"Vida Do Inimigo: [green]{enemy.life}:{enemy.maxlife}[/]"
        )

class Solo(jogador):
    def __init__(self, name, maxlife, life):
        super().__init__(name, maxlife, life)
        self.attacksmethods = ["Soco", "Chute"]

    def receive_damage(self, damage):
        fator = random.randint(1, damage)
        self.life -= fator

        if self.life <= 0:
            self.life = 0

        print(
            f" [!] [blue]{self.name}[/] "
            f"Recebeu [red]dano de {fator}[/] "
        )

    def send_damage(self, target, strength=50):
        if self.life > 0 and target.life > 0:
            attack = self.attacksmethods[
                random.randrange(0, len(self.attacksmethods))
            ]

            print(
                f"[!] {self.name} atacou "
                f"{target.name} com um {attack}"
            )

            resultado = random.choice([0, 1])

            if resultado == 1:
                print(
                    f"[!] {self.name} Acertou um ataque "
                    f"contra {target.name}!"
                )

                target.receive_damage(strength)

            elif resultado == 0:
                print(
                    f"[!] {self.name} Errou um ataque "
                    f"contra {target.name}!"
                )

        else:
            print(
                f"[red][!][/]O ataque {self.name} -> "
                f"{target.name} não pode acontecer."
            )

    def heartbeat(self):
        pass

    def status(self):
        print(
            f"[red][!][/] [blue]{self.name}[/]"
            f"Vida: [green]{self.maxlife}:{self.life}[/]"
            f"Ataques: [red]{self.attacksmethods}[/]"

            f"[red][!] [Blue]{enemy.name}[/]"
            f"Vida Do Inimigo: [green]{enemy.life}:{enemy.maxlife}[/]"
        )