__author__ = 'Cyberbreno'  # :p

from criteria import *
from interface import *
from arquivo import *


# PROGRAM LOOP_________________________________________________________________:
while True:
    # Dataset file_____________________________________________________________:
    ArqP = input('Dataset: ')

    if ArqP == '0' or ArqP == 'sair':
        break
    else:
        test = arqteste(ArqP)

    # Call the functions_______________________________________________________:
    if test:
        while True:
            cabecalho(f'Dataset com {count(ArqP, ">")} sequências')
            resp = menu(['Contar', 'Renomear', 'Deletar sequencias', 'Renomear sequencias específicas',
                         'Renomear Dataset', 'Deletar uma lista de sequencias', 'Renomear árvore', 'Sair'])

            if resp == 1:
                par1 = input('Parametro: ')

                seqcont = find(ArqP, par1)

            elif resp == 2:
                name2 = input('Nome para as sequencias: ')

                seqname = rename(ArqP, name2)
                createArq(ArqP, ''.join(seqname))

            elif resp == 3:
                par3 = input('Parametro: ')

                seqpar = cleaner(ArqP, par3)
                createArq(ArqP, ''.join(seqpar))

            elif resp == 4:
                par4 = input('Parametro: ')
                name4 = input('Nome para as sequencias: ')

                seqSname = namEsp(ArqP, name4, par4)
                createArq(ArqP, ''.join(seqSname))

            elif resp == 5:
                datrename(ArqP)

            elif resp == 6:
                listdel(ArqP, 'list.txt')

            elif resp == 7:
                rename_tree(ArqP)

            elif resp == 8:
                break

    else:
        print(linha())
        print("Arquivo nao encontrado".center(42))
        print(linha())
