# Importações 
from random import randint
from sys import exit as sair
from time import sleep
import os

# Funções


def menu():

    os.system("cls")
    print('-' * 42)
    print('Jogo da Velha'.center(42))
    print('-' * 42)
    print('0 - Sair')
    print('1 - Jogar')
    print('-' * 42)

    while True:
        pergunta = leiaint('Escolha: ')
        if pergunta >= 0 and pergunta <= 1:
            break
    if pergunta == 0:
        print('-' * 42)
        print('Finalizando'.center(42))
        print('-' * 42)
        sleep(3)
        os.system("cls")
        sair()
    elif pergunta == 1:
        print('-' * 42)
        print('Iniciando'.center(42))
        print('-' * 42)
        sleep(3)
        iniciar()


def iniciar():

    while True:
        os.system("cls")
        matriz()
        while True:
            linha = leiaint('Em qual linha desejar marcar? ')-1
            if linha >= 0 and linha <= 2:
                break
            print('Linha inválida. Por favor tente novamente.')

        while True:
            coluna = leiaint('Em qual coluna escolhida deseja marcar? ')-1
            if coluna >= 0 and coluna <= 2:
                break
            print('Coluna inválida. Por favor tente novamente.')

        print()

        X = marcarX(linha, coluna)
        jogoX = verificarX()
        if jogoX == True and X == True:
            marcarO()
            jogoO = verificarO()  

        tam = verificartam()
        if tam == True:
            print('O jogo empatou! :/')
            print('-' * 42)
            sleep(3.5)
            menu()
        if jogoX == False:
            print('Você ganhou! :)')
            print('-' * 42)
            sleep(3.5)
            menu()
        if jogoO == False:
            print('A máquina ganhou! :(')
            print('-' * 42)
            sleep(3.5)
            menu()
        print('-' * 42)
        sleep(3.5)
        
        
def matriz():
    print('-' * 42)
    for linha in range(3):
        for c in range(3):
            print(f'     [{matrizlista[linha][c]:^5}]', end='')
        print()
    print('-' * 42)


def marcarX(linha, coluna):
    if 'X' not in matrizlista[linha][coluna] and 'O' not in matrizlista[linha][coluna]:
            print(f'Você marcou X na linha {linha+1} coluna {coluna+1}.')
            matrizlista[linha][coluna] = 'X'
            return True
    else:
        print(f'A linha {linha+1} coluna {coluna+1} está marcada.')
        return False


def verificarX():
    for c in range(3):
        if 'X' in matrizlista[c][0] and 'X' in matrizlista[c][1] and 'X' in matrizlista[c][2] or 'X' in matrizlista[0][c] and 'X' in matrizlista[1][c] and 'X' in matrizlista[2][c]:
            return False
    if 'X' in matrizlista[0][0] and 'X' in matrizlista[1][1] and 'X' in matrizlista[2][2] or 'X' in matrizlista[0][2] and 'X' in matrizlista[1][1] and 'X' in matrizlista[2][0]:
        return False
    return True


def marcarO():
    while True:
        linha = randint(0,2)
        coluna = randint(0, 2)
        if 'X' not in matrizlista[linha][coluna] and 'O' not in matrizlista[linha][coluna]:
            print(f'O computador marcou O na linha {linha+1} coluna {coluna+1}.')
            matrizlista[linha][coluna] = 'O'
            break


def verificarO():
    for c in range(3):
        if 'O' in matrizlista[c][0] and 'O' in matrizlista[c][1] and 'O' in matrizlista[c][2] or 'O' in matrizlista[0][c] and 'O' in matrizlista[1][c] and 'O' in matrizlista[2][c]:
            return False
    if 'O' in matrizlista[0][0] and 'O' in matrizlista[1][1] and 'O' in matrizlista[2][2] or 'O' in matrizlista[0][2] and 'O' in matrizlista[1][1] and 'O' in matrizlista[2][0]:
        return False
    return True


def verificartam():
    tam = 0
    for linha in range(3):
        for c in range(3):
            if matrizlista[linha][c] != '':
                tam += 1
    if tam == 9:
        return True
    return False


def leiaint(número):
    while True:
        try:
            número = int(input(f'{número}'))
        except:
            print(f'\033[31mPor favor digite apenas número inteiro.\033[m')
        else:
            return número


# Matriz

matrizlista = [['', '', ''], ['', '', ''], ['', '', '']]

# Iniciar
menu()