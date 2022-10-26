import os
from funcoes.visual2 import visualApp
from funcoes.visual2 import players
from funcoes.visual2 import mostrarRecords
answer=1
while answer ==1:
    visualApp("    Seja bem vindo")
    players("Digite o nome do competidor: ","Digite o nome do Desafiante: ", "Desafiante, informe a palavra chave: ")
    mostrarRecords("   Histórico das partidas    ")
    try:
        print("Escolha 1 para jogar novamente ou")
        print("escolha 2 para sair do jogo")
        answer=int(input("Sua escolha: "))
        if answer==1:
            print("Vamos novamente!")
    except:
        print("Coloque um valor válido")
    if  answer == 2:
        break