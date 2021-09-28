# Hazak
Simple bioinformatic script to clean, organize and simplify the work with large datasets from uncurated databases. 

Features
- Easily delete from the dataset low-quality sequences, such as sequences with few residues then espected
- Also delete sequences with keywords that evidence low-quality data, such as 'partial', 'hypothetical', and anyother 
you want.
- Put prefixes in sequences with specific parameters to make the data analysis in aligments and trees much easy  
- Direct delete a list of sequences 

usage:
    hazak [-c PARAMETER] [-e PARAMETER] [-p PARAMETER PREFIX] [-l LIST_FILE] [-r RESIDUES_THRESHOLD] dataset_input dataset_output

positional arguments:
    input file          must be the last but one argument (.fasta, .fastq)
    output file         last argument (.fasta, .fastq)

optional arguments:
    --help              show this message

    -c                  count how many sequences have the given parameter

    -e                  count and delete the sequences with the given parameter

    -p                  find the sequences with the given parameter, them put a prefix into the name of the sequence 
                        (right before the '>')

    -l                  delete from the dataset the sequences in the given file

    -r                  delete all sequences with less residues them the given threshold


A compilled of some simple scripts that I used to save some time when running bioinformatic pipelines with protein 
datasets from uncurated databases.

Finally, contact me if you have ANY suggestion, I am quite new with programming and all of this. :)