def count(arq, parametro):
    cont = 0
    rem = []
    k = 0

    for c, line in enumerate(arq):
        if f'{parametro}'.lower() in line.lower():
            cont += 1
            rem.append(c)
            k = 1
        elif k == 1:
            if '>' in line:
                k = 0
            else:
                rem.append(c)

    print(f'The parameter {parametro} was found in {cont} sequences.')
    return cont


# Count how many sequences have the parameter, can delete this sequences_______:
def find(arq, parametro):
    cont = 0
    rem = []
    k = 0

    for c, line in enumerate(arq):
        if f'{parametro}'.lower() in line.lower() and '>' in line[0]:
            cont += 1
            rem.append(c)
            k = 1
            print(f'Parameter founded in: {line.strip()}')
        elif k == 1:
            if '>' in line:
                k = 0
            else:
                rem.append(c)

    print(f'{cont} sequences has the parameter "{parametro}"')
    for p in rem[::-1]:
        del arq[p]
    return arq


# Rename sequences with the parameter__________________________________________:
def nprefix(arq, parametro, name):
    rem = []
    new = []
    num = 0

    for c, line in enumerate(arq):
        if f'{parametro}'.lower() in line.lower() and '>' in line[0]:
            print(f'The sequence "{line.strip()}" will be renamed')
            new.append(line.replace('>', f'>{name}'))
            rem.append(c)

    for p in rem[::-1]:
        del arq[p]
        arq.insert(p, new[num])
        num += 1

    return arq


# Delete sequences from a given file___________________________________________:
def listdel(arqdataset, arqlista):
    lista = open(arqlista, 'r')
    rem = []
    p = 0

    for seq in lista.readlines():
        parametro = seq[:-1]

        for c, line in enumerate(arqdataset):
            if f'{parametro}'.lower() in line.lower() and '>' in line[0]:
                rem.append(c)
                p = 1

            elif p == 1:
                if '>' in line[0]:
                    p = 0

                else:
                    rem.append(c)

    rems = sorted(rem)
    for x in rems[::-1]:
        del arqdataset[x]

    return arqdataset


# Script que conte quantos residuos tem cada seq e apague as seq abaixo de um threshold estabelecido
def rescount(arqdataset, thold):
    cur_line = []
    cur_seq = []
    all_seq = []
    all_line = []
    tseqs = []

    for x, line in enumerate(arqdataset):
        if '>' in line[0]:
            all_seq.append((''.join(cur_seq), len(all_seq)))
            all_line.append(cur_line)
            cur_line = []
            cur_seq = []
            cur_line.append(x + 1)

        elif '\n' not in line[0]:
            if x+1 == len(arqdataset):
                cur_line.append(x+1)
                cur_seq.append(line.strip('\n'))
                all_seq.append((''.join(cur_seq), len(all_seq)))
                all_line.append(cur_line)

            else:
                cur_seq.append(line.strip('\n'))
                cur_line.append(x+1)
        else:
            pass

    for seq in all_seq[1::]:
        # seq[0] is the sequence, [1] the number of the sequence
        print(seq[1], len(seq[0]), seq[0])
        if len(seq[0]) <= thold:
            tseqs.append(all_line[seq[1]])

    for line in tseqs[::-1]:
        for p in line[::-1]:
            del arqdataset[p-1]


""" Script que conte quantas seqs tem cada nome (split no nome da seq)
"""
if __name__ == '__main__':
    pass
