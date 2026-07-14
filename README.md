<div align="center">

```text
██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝

███████╗ ██████╗ █████╗ ██╗██╗
██╔════╝██╔════╝██╔══██╗██║██║
███████╗██║     ███████║██║██║
╚════██║██║     ██╔══██║██║██║
███████║╚██████╗██║  ██║██║███████╗
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝
```

# DragonScail

### Um RPG de fantasia medieval desenvolvido em Python

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow?style=for-the-badge)](#)
[![GitHub](https://img.shields.io/badge/GitHub-Sickzs-181717?style=for-the-badge\&logo=github)](https://github.com/Sickzs)
[![License](https://img.shields.io/badge/Licen%C3%A7a-A%20definir-lightgrey?style=for-the-badge)](#licença)

</div>

---

## Sobre o projeto

**DragonScail** é um RPG de texto ambientado em um mundo de fantasia medieval.

Durante muitos anos, acreditou-se que os dragões haviam desaparecido. Porém, aldeias começaram a ser atacadas por criaturas marcadas com símbolos antigos.

Rumores dizem que alguém está tentando despertar o último Grande Dragão.

O jogador deverá explorar esse mundo, enfrentar criaturas, conseguir equipamentos e tomar decisões que poderão mudar o rumo de sua jornada.

> O projeto está em desenvolvimento e está sendo criado como forma de aprender Python, orientação a objetos e desenvolvimento de jogos em terminal.

---

## História

```text
Durante muitos anos, acreditou-se que os dragões
haviam desaparecido...

Porém, aldeias começaram a ser atacadas por criaturas
marcadas com símbolos antigos.

Rumores dizem que alguém está tentando despertar
o último Grande Dragão.

Sua jornada começa agora...
```

---

## Funcionalidades

### Em desenvolvimento

* Sistema de criação de personagem
* Campanha principal em modo texto
* Sistema de vida, mana, ataque e defesa
* Combate por turnos
* Inimigos com diferentes atributos
* Inventário e equipamentos
* Escolhas durante a história
* Sistema de dano normal e crítico
* Possibilidade de fugir das batalhas

### Planejado

* Sistema de níveis e experiência
* Classes de personagem
* Missões secundárias
* Vilas, florestas, cavernas e masmorras
* Loja e sistema de moedas
* Salvamento e carregamento da campanha
* Multiplayer local
* Multiplayer online
* Diferentes finais para a história

---

## Menu do jogo

```text
╔════════════════════════════╗
║        DRAGON SCAIL        ║
╚════════════════════════════╝

[ 1 ] Jogar sozinho
[ 2 ] Multiplayer local
[ 3 ] Multiplayer online
[ 4 ] Carregar campanha
[ 5 ] Configurações
[ 0 ] Sair
```

---

## Tecnologias

| Tecnologia                      | Utilização                          |
| ------------------------------- | ----------------------------------- |
| Python                          | Linguagem principal                 |
| Programação orientada a objetos | Personagens, inimigos e itens       |
| JSON                            | Salvamento de dados planejado       |
| Rich                            | Formatação e cores no terminal      |
| Random                          | Ataques, danos e eventos aleatórios |
| Git                             | Controle de versão                  |
| GitHub                          | Hospedagem do código                |

---

## Estrutura planejada

```text
DragonScail/
├── main.py
├── campanha.py
├── README.md
├── jogo/
│   ├── __init__.py
│   ├── jogador.py
│   ├── inimigos.py
│   ├── itens.py
│   └── batalha.py
└── dados/
    └── saves/
```

A estrutura poderá mudar conforme o desenvolvimento do projeto avançar.

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Sickzs/DragonScail.git
```

### 2. Entre na pasta

```bash
cd DragonScail
```

### 3. Execute o jogo

```bash
python main.py
```

Em algumas distribuições Linux, pode ser necessário usar:

```bash
python3 main.py
```

---

## Ambiente virtual

Para criar um ambiente virtual:

```bash
python -m venv .venv
```

Ative no Linux:

```bash
source .venv/bin/activate
```

Ative no Windows:

```powershell
.venv\Scripts\activate
```

Depois, instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Exemplo de combate

```text
O que você deseja fazer?

[ 1 ] Atacar
[ 2 ] Ver inventário
[ 3 ] Ver status
[ 0 ] Fugir

Digite sua escolha: 1

Você atacou o Goblin com uma espada velha.

O Goblin recebeu 12 de dano!
Vida restante: 18/30
```

---

## Status do desenvolvimento

```text
[████░░░░░░] Em desenvolvimento
```

O projeto ainda está em uma fase inicial. Sistemas, nomes, arquivos e mecânicas poderão ser modificados.

---

## Objetivos de aprendizado

Este projeto está sendo utilizado para praticar:

* Variáveis e tipos de dados
* Estruturas condicionais
* Laços de repetição
* Funções
* Listas e dicionários
* Classes e objetos
* Herança
* Classes abstratas
* Organização de projetos
* Manipulação de arquivos
* Git e GitHub

---

## Contribuições

O DragonScail é um projeto pessoal de aprendizado, mas sugestões e correções são bem-vindas.

Para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua alteração.
3. Faça suas modificações.
4. Envie um pull request explicando as mudanças.

---

## Autor

Desenvolvido por **Sickzs**.

[![GitHub](https://img.shields.io/badge/GitHub-Sickzs-181717?style=for-the-badge\&logo=github)](https://github.com/Sickzs)

---

## Licença

A licença do projeto ainda não foi definida.

Enquanto nenhuma licença for adicionada, o código permanece protegido pelos direitos autorais do autor e não deve ser copiado, redistribuído ou modificado sem autorização.

---

<div align="center">

```text
$ python main.py

Inicializando DragonScail...
Carregando mundo...
Preparando sua jornada...

Sua aventura começa agora.
```

**Feito com Python, terminal e muita vontade de aprender.**

</div>
