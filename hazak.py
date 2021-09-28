from criteria import *
import sys


def run():
    doc = ('\n'
           'usage: \n'
           '     hazak [-c PARAMETER] [-e PARAMETER] [-p PARAMETER PREFIX] [-l LIST_FILE] [-r RESIDUES_THRESHOLD] '
           'dataset_input dataset_output \n \n'
           'positional arguments:\n'
           '     input file          must be the last but one argument (.fasta, .fastq)\n'
           '     output file         last argument (.fasta, .fastq)\n \n'
           'optional arguments:\n'
           '     --help              show this message\n'
           '     -c                  count how many sequences have the given parameter\n'
           '     -e                  count and delete the sequences with the given parameter\n'
           '     -p                  find the sequences with the given parameter, them put a prefix into the name of'
           'the sequence\n'
           '     -l                  delete from the dataset the sequences in the given file\n'
           '     -r                  delete all sequences with less residues them the given threshold\n')

    if len(sys.argv) == 1:
        print(doc)

    else:
        arq = open(sys.argv[-2], 'r').readlines()

        for arg in sys.argv:
            if arg == '--help':
                print(doc)
                break

            elif arg == '-c':
                par = sys.argv[sys.argv.index(arg) + 1]
                count(arq, par)

            elif arg == '-e':
                par = sys.argv[sys.argv.index(arg) + 1]
                arq = find(arq, par)

            elif arg == '-p':
                par = sys.argv[sys.argv.index(arg) + 1]
                name = sys.argv[sys.argv.index(arg) + 2]
                arq = nprefix(arq, par, name)

            elif arg == '-l':
                arqlista = sys.argv[sys.argv.index(arg) + 1]
                arq = listdel(arq, arqlista)

            elif arg == '-r':
                thold = int(sys.argv[sys.argv.index(arg) + 1])
                arq = rescount(arq, thold)

        narq = open(sys.argv[-1], 'w')
        narq.write(''.join(arq))


if __name__ == '__main__':
    run()
