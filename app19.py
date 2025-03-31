'''19. Faça o jogo de Jokenpô multiplayer.'''

import random

jogador1 = input("Digite o nome do jogador 1: ")
jogador2 = input("Digite o nome do jogador 2: ")

jogadas = ["pedra", "papel", "tesoura"]

jogada1 = input("Digite a jogada do jogador 1: ")
jogada2 = input("Digite a jogada do jogador 2: ")

if jogada1 not in jogadas or jogada2 not in jogadas:
    print("Jogada inválida!")
    exit()

print(f"{jogador1} jogou {jogada1}")
print(f"{jogador2} jogou {jogada2}")

if jogada1 == jogada2:
    print("Empate!")
elif (jogada1 == "pedra" and jogada2 == "tesoura") or (jogada1 == "papel" and jogada2 == "pedra") or (jogada1 == "tesoura" and jogada2 == "papel"):
    print(f"{jogador1} ganhou!")
else:
    print(f"{jogador2} ganhou!")