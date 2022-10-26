import os
def visualApp (mensagem):
    print("----"*6)
    print(mensagem)
    print("----"*6)
def players(mensagem, mensagem2, mensagem3):
    recordes=open("records.jogo","a")
    recordes.write("\nCompetidor: ")
    competidor=input(mensagem)
    recordes.write("{} \n".format(competidor))
    recordes.write("Desafiante: ")
    desafiante=input(mensagem2)
    recordes.write("{} \n".format(desafiante))
    recordes.close()
    os.system("cls")
    print("O competidor:", competidor,)
    print("O desafiante:", desafiante,)
    chance = 5
    recordes=open("records.jogo", "a")
    words=(input(mensagem3))
    recordes.write("A palavra foi: ")
    recordes.write(words)
    recordes.close()
    words=list(words)
    dicas=[]
    dicas.append(input("Dica 1: "))
    dicas.append(input("Dica 2: "))
    dicas.append(input("Dica 3: "))
    os.system("cls")
    asterisco=[]
    for i in range(len(words)):
        asterisco.append("*")
    print("A palavra tem {} letras: ".format(len(words)))
    print(asterisco)
    print("O competidor tem apenas 5 chances para errar e pode pedir 3 dicas!")
    limitador=0
    dica=0
    erros=0
    while limitador ==0:
        if "*" not in asterisco:
            print("Meus parabéns, o competidor ganhou!")
            recordes=open("records.jogo", "a")
            recordes.write("\nO ganhador foi o competidor: ")
            recordes.write(competidor)
            recordes.write("\n       Novo jogo \n")
            recordes.close()
            break
        if chance ==0:
            print("O desafiante ganhou!")
            recordes.write("O ganhador foi o Desafiador: ")
            recordes.write(desafiante)
            recordes.write("\n       Novo jogo \n")
            recordes.close()
            break
        print("A tecla 0 solicita a dica")
        print("A tecla 1 segue para o jogo")
        choice=2
        while choice >1:
            try:
                choice=int(input("Sua resposta: "))
            except:
                print("Informe um valor!")
        while chance > 0:
            if choice == 1:
                if chance == 0:
                    print("Suas chances acabaram! O competidor perdeu.")
                    break
                print("Erros:",erros)
                print(dica)
                letra=(input("informe a letra, competidor: "))
                os.system("cls")
                contagem = words.count(letra)
                for i in range(contagem):
                    if letra in words:
                        indice=int(words.index(letra))
                        asterisco[indice] = letra
                        if contagem> 1:
                            words[indice]="*"
                if letra not in words:
                    chance=chance-1
                    erros=erros+1
                    if contagem>0:
                        chance=chance+1
                        erros=erros-1
                print("Erros:", erros)
                print("Chances:", chance)
                print("A palavra é:")
                print(asterisco)
                break
            if choice ==0 and dica <3:
                print("Dica:",dicas[dica])
                dica=dica+1
                letra=(input("informe a letra, competidor: "))
                os.system("cls")
                contagem = words.count(letra)
                for i in range(contagem):
                    if letra in words:
                        indice=int(words.index(letra))
                        asterisco[indice] = letra
                        if contagem> 1:
                            words[indice]="*"
                if letra not in words:
                    chance=chance-1
                    erros=erros+1
                    if contagem>0:
                        chance=chance+1
                        erros=erros-1
                print("Erros:", erros)
                print("Chances:", chance)
                print("A palavra é:")
                print(asterisco)
                break
            if dica ==3:
                print("Suas chances acabaram!")
                letra=(input("informe a letra, competidor: "))
                os.system("cls")
                contagem = words.count(letra)
                for i in range(contagem):
                    if letra in words:
                        indice=int(words.index(letra))
                        asterisco[indice] = letra
                        if contagem> 1:
                            words[indice]="*"
                if letra not in words:
                    chance=chance-1
                    erros=erros+1
                    if contagem>0:
                        chance=chance+1
                        erros=erros-1
                print("Erros:", erros)
                print("Chances:", chance)
                print("A palavra é:")
                print(asterisco)
                break
def mostrarRecords(mensagem):
    print(mensagem)
    recordes=open("records.jogo", "r")
    conteudo=recordes.readlines()
    for linhas in conteudo:
        print(linhas)