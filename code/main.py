# Importações 
from random import randint
from sys import exit as sair

# Funções

def iniciar():
    print('-' * 42)
    print('Iniciar'.center(42))
    print('-' * 42)
    matriz()
    jogo = True
    while True:

        X = False

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

        X = marcarX(linha, coluna, jogo)
        if jogo == True and X == True:
            marcarO()
        if jogo == False:
            sair()
        matriz()
        
def matriz():
    print()
    for linha in range(3):
        for c in range(3):
            print(f'[{matrizlista[linha][c]:^5}]', end='')
        print()
    print()


def marcarX(linha, coluna, jogo):
    if 'X' not in matrizlista[linha][coluna] and 'O' not in matrizlista[linha][coluna]:
            print(f'Você marcou X na linha {linha+1} coluna {coluna+1}.')
            matrizlista[linha].insert(coluna, 'X')
            return jogo == True
    else:
        print(f'A linha {linha+1} coluna {coluna+1} está marcada.')


def marcarO():
    while True:
        linha = randint(0, 2)
        coluna = randint(0, 2)
        if 'X' not in matrizlista[linha][coluna] and 'O' not in matrizlista[linha][coluna]:
            print(f'O computador marcou O na linha {linha+1} coluna {coluna+1}.')
            matrizlista[linha].insert(coluna, 'O')
            break


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
iniciar()