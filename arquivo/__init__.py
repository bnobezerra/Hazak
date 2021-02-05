from interface import *


def arqteste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArq(name, write):
    try:
        a = open(name, 'w')
        a.write(write)
        a.close()
    except:
        print('[ERRO] Não foi possível criar o arquivo!')
    else:
        print(f'Arquivo {name} criado/ alterado com sucesso!')


def readArq(name):
    try:
        a = open(name, 'r')
    except:
        print('[ERRO] Não foi possível ler o arquivo!')
    else:
        return a

