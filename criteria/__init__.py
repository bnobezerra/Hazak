from arquivo import *
import re


def count(arq, parametro):
    arqteste(arq)
    a = readArq(arq)
    b = a.readlines()
    cont = 0
    rem = []
    k = 0

    for c, line in enumerate(b):
        if f'{parametro}'.lower() in line.lower():
            cont += 1
            rem.append(c)
            k = 1
        elif k == 1:
            if '>' in line:
                k = 0
            else:
                rem.append(c)

    return cont


# Rename all sequences in the dataset__________________________________________:
def rename(arq, name):
    a = readArq(arq)
    b = a.read()

    if '>' in b:
        c = b.replace('>', f'>{name}')
        print(c)
        asq = input('Está certo? [Y/N]').lower()

        if asq == 'y':
            return c

        elif asq == 'n':
            print('????sei nao entao bixo')

        else:
            print('Por favor, digite apenas "y" ou "n"')


# Delete sequences with the especific parameter________________________________:
def cleaner(arq, parametro):
    arqteste(arq)
    a = readArq(arq)
    b = a.readlines()
    rem = []
    k = 0

    # For each line, it tests if the line have the parameter___________________:
    for c, line in enumerate(b):
        if f'{parametro}'.lower() in line.lower() and '>' in line:
            print(f'The sequence {line} will be removed')
            rem.append(c)
            k = 1

        elif k == 1:
            if '>' in line:
                k = 0
            else:
                rem.append(c)

    for p in rem[::-1]:
        del b[p]

    return b


# Count how many sequences have the parameter, can delete this sequences_______:
def find(arq, parametro):
    arqteste(arq)
    a = readArq(arq)
    b = a.readlines()
    cont = 0
    rem = []
    k = 0

    for c, line in enumerate(b):
        if f'{parametro}'.lower() in line.lower():
            cont += 1
            rem.append(c)
            k = 1
            print(f'A sequencia {line} tem o parametro!')
        elif k == 1:
            if '>' in line:
                k = 0
            else:
                rem.append(c)

    print(f'O parametro "{parametro}" foi encontrado {cont} vezes')

    res = input(f'Deseja apagar essas sequências? [Y/N]').lower()

    if res == 'y':
        for p in rem[::-1]:
            del b[p]

        createArq(arq, ''.join(b))
        # The file is created in the function because this func dont return files all the time its used


# Rename sequences with the parameter__________________________________________:
def namEsp(arq, name, parametro):
    arqteste(arq)
    a = readArq(arq)
    b = a.readlines()
    rem = []
    new = []
    num = 0

    for c, line in enumerate(b):
        if '>' in line.lower():
            if f'{parametro}'.lower() in line.lower():
                print(f'A sequencia "{line}" tem o parametro')
                new.append(line.replace('>', f'>{name}'))
                rem.append(c)

    for p in rem[::-1]:
        del b[p]
        b.insert(p, new[num])
        num += 1

    print(b)
    return b


# Delete sequences that are in the 'list.txt'__________________________________:
def listdel(arqdataset, arqlist):
    a = readArq(arqlist)
    b = a.readlines()
    print(arqdataset)
    j = readArq(arqdataset)
    k = j.readlines()

    rem = []
    p = 0

    for line in b:
        parametro = line[:-1]
        print(parametro)

        for c, line1 in enumerate(k):
            if f'{parametro}'.lower() in line1.lower():
                rem.append(c)
                p = 1

            elif p == 1:
                if '>' in line1:
                    p = 0

                else:
                    rem.append(c)

    remS = sorted(rem)
    for x in remS[::-1]:
        del k[x]

    createArq(f'new_{arqdataset}', ''.join(k))


# Rename sequences in order to the file 'filos.txt'____________________________:
def datrename(arqdataset):
    a = readArq(arqdataset)
    b = a.readlines()
    arqList = readArq('filos.txt')
    filos = arqList.readlines()
    names = []
    number = []
    rem = []
    new = []
    num = 0
    old = 0

    for line in filos:
        name = line.split('\n')
        names.append(name[0])
        number.append(int(input(f'Quantity of {name[0]}: ')))

    for d, name in enumerate(names):
        count = 1
        index = number[d]
        index += old

        for c, line in enumerate(b):
            if '>' in line:
                if old < count <= index:
                    new.append(line.replace('>', f'>{name}'))
                    rem.append(c)
                    count += 1

                else:
                    count += 1

        old = 0
        old += index

    print(names)
    for p in rem:
        del b[p]
        b.insert(p, new[num])
        num += 1

    createArq(f'new_{arqdataset}', ''.join(b))


# Rename sequences in the tree in order to ????????____________________________:
def rename_tree(name):
    lista = open('lista_species.txt', 'r')
    final = open('datadafinaDAT.fasta', 'w')
    lista_r = lista.readlines()
    old_name = ''
    new_name = ''
    trade = []
    rem = []
    old = ''
    filos = ['Amoebozoa', 'arachnids', 'cephalochordata', 'cnidaria', 'crustacea', 'echinodermata', 'insects', 'mamals',
             'Monotreme', 'mollusca', 'nematoda', 'platyhelminthes', 'tardigrades', 'tunicate', 'xiphosura',
             'cartilaginous', 'brachiopoda', 'bonyfishes', 'bird', 'amphibia', 'Reptila', 'Lizard', 'Alligator',
             'Turtles', 'Viridiplantae', 'Fungi', 'Euglenozoa', 'Ciliates', 'Choanoflagelates', 'Capsaspora']

    z = 0
    c = 0
    for line in lista_r:
        if c == 0:
            old_name = line.split('\n')
            c += 1
            """for filo in filos:
                if filo in old_name[0]:
                    old = old_name[0].replace(filo, '')
                    print(old)"""

        elif c == 1:
            new_name = line.split('\n')[0]
            n1_name = new_name.strip()
            n2_name = new_name.split()
            new = f'{n1_name[0]}._{n2_name[1]}_{old_name[0]}'
            c = 0
            trade.append((old_name[0], f"{new.replace(' ', '_')}"))

    a = open(name, 'r')
    arq = a.read()
    d = 0
    for taxon in trade:
        if taxon[0] in arq and d == 0:
            f = re.sub(taxon[0], taxon[1], arq)
            d += 1

        elif taxon[0] in f and d == 1:
            f = re.sub(taxon[0], taxon[1], f)
    print(f)

    final.write(f)
    final.close()
