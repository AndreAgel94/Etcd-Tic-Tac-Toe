import os
import platform
import socket
import time



clean = ('clear', 'cls')[platform.system() == 'Windows']

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def resetTabuleiro():
    tabuleiro = ['1', '2', '3',
                 '4', '5', '6',
                 '7', '8', '9']
    return tabuleiro

def mostrarTabuleiro(tabuleiro):
    print(" %s | %s | %s " % (tabuleiro[0],tabuleiro[1],tabuleiro[2]))
    print("---+---+---")
    print(" %s | %s | %s " % (tabuleiro[3],tabuleiro[4],tabuleiro[5]))
    print("---+---+---")
    print(" %s | %s | %s " % (tabuleiro[6],tabuleiro[7],tabuleiro[8]))


def atualizaTabuleiro(tabuleiro, posicaoDajogada, letra):
    tabuleiro[posicaoDajogada-1] = letra
    return tabuleiro

def arrumaTabuleiro(tabString):
  tabuleiro = []
  for index, value in enumerate(tabString):
    if value == '0':
        tabuleiro.append(str(index+1))
    else:
        tabuleiro.append(value)

  return tabuleiro

def inputPosicaoValida(tabuleiro):
    while True:
        try:
            pos = int(input("Qual posicao quer jogar? "))
            if 0 < pos < 10:
                if tabuleiro[pos-1] != "O" and tabuleiro[pos-1] != "X":
                    return pos
                else:
                    print("Posicao invalida, alguem ja jogou nessa posicao!")
            else:
                print("Posicao invalida, jogue de 1 a 9!")
        except:
            print("Caractere invalido, deve ser um inteiro de 1 a 9!")


def jogo(me):
    mySign = ''
    hisSign = ''
    tabuleiro = resetTabuleiro()
    pontuacao = 0
    while True:
        me.setblocking(True)
        message = me.recv(1024).decode()
        if message == "suaVez":
            os.system(clean)
            me.setblocking(False)
            flush_input()
            print("Sua Vez!")
            mostrarTabuleiro(tabuleiro)
            pos = inputPosicaoValida(tabuleiro)
            me.send(str(pos).encode())
            posicao = int(pos)
            os.system(clean)
            tabuleiro = atualizaTabuleiro(tabuleiro, posicao, mySign)
            mostrarTabuleiro(tabuleiro)
        elif message == "aguardeRival":
            print("Esperando um rival...")
        elif message == "aguardeSuaVez":
            print("Espere o oponente jogar!")
        elif message == "jx":
            print("Conectado! Voce eh o X!")
            mySign = 'X'
            hisSign = 'O'
        elif message == "jo":
            nomeO = input("Digite seu nome: ")
            me.send(str(nomeO).encode())
            print("Conectado! Voce eh o O!")
            mySign = 'O'
            hisSign = 'X'
        elif message == "ganhouRodada":
            pontuacao += 1
            print("Voce ganhou uma rodada!\nSua pontuacao: " + str(pontuacao))
            print("Reiniciando o jogo... Quem ganhou comeca!")
            tabuleiro = resetTabuleiro()
            time.sleep(1)
        elif message == "perdeuRodada":
            print("Voce perdeu uma rodada!\nSua pontuacao: " + str(pontuacao))
            print("Reiniciando o jogo... Quem ganhou comeca!")
            tabuleiro = resetTabuleiro()
            time.sleep(1)
        elif message == "empate":
            print("Empate!\nSua pontuacao: " + str(pontuacao))
            print("Reiniciando o jogo...!")
            tabuleiro = resetTabuleiro()
            time.sleep(1)
        elif message == "1" or message == "2" or message == "3" or message == "4" or message == "5" or message == "6" or message == "7" or message == "8" or message == "9":
            atualizaTabuleiro(tabuleiro, int(message), hisSign)
        elif message == "ganhouJogo":
            pontuacao += 1
            print("Voce ganhou o jogo!!!\nPontuacao: " + str(pontuacao))
            print("Desconectando...")
            return None
        elif message == "perdeuJogo":
            print("Voce perdeu o jogo!!!\nPontuacao: " + str(pontuacao))
            print("Desconectando...")
            return None
        elif message[:14] == "recuperaEstado":
            tabString = message[14:23]
            tabuleiro = arrumaTabuleiro(tabString)
            pontuacao = int(message[23])


def main():
    while True:
        try:
            host = "localhost"
            port = input("Digite a porta do servidor: ")
            me = socket.socket()
            me.connect((host, int(port)))
            jogo(me)
            break
        except:
            print("IP ou porta invalidos ou servidor fora do ar!")

    me.close()


if __name__ == "__main__":
    main()
