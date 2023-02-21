#Name - Rishi Vora
#Roll No - MS21113

codons = {
    "UUU": "Phe",
    "CUU": "Leu",
    "AUU": "Ile",
    "GUU": "Val",
    "UUC": "Phe",
    "CUC": "Leu",
    "AUC": "Ile",
    "GUC": "Val",
    "UUA": "Leu",
    "CUA": "Leu",
    "AUA": "Ile",
    "GUA": "Val",
    "UUG": "Leu",
    "CUG": "Leu",
    "AUG": "Met",
    "GUG": "Val",
    "UCU": "Ser",
    "CCU": "Pro",
    "ACU": "Thr",
    "GCU": "Ala",
    "UCC": "Ser",
    "CCC": "Pro",
    "ACC": "Thr",
    "GCC": "Ala",
    "UCA": "Ser",
    "CCA": "Pro",
    "ACA": "Thr",
    "GCA": "Ala",
    "UCG": "Ser",
    "CCG": "Pro",
    "ACG": "Thr",
    "GCG": "Ala",
    "UAU": "Tyr",
    "CAU": "His",
    "AAU": "Asn",
    "GAU": "Asp",
    "UAC": "Tyr",
    "CAC": "His",
    "AAC": "Asn",
    "GAC": "Asp",
    "UAA": "Stop",
    "CAA": "Gln",
    "AAA": "Lys",
    "GAA": "Glu",
    "UAG": "Stop",
    "CAG": "Gln",
    "AAG": "Lys",
    "GAG": "Glu",
    "UGU": "Cys",
    "CGU": "Arg",
    "AGU": "Ser",
    "GGU": "Gly",
    "UGC": "Cys",
    "CGC": "Arg",
    "AGC": "Ser",
    "GGC": "Gly",
    "UGA": "Stop",
    "CGA": "Arg",
    "AGA": "Arg",
    "GGA": "Gly",
    "UGG": "Trp",
    "CGG": "Arg",
    "AGG": "Arg",
    "GGG": "Gly"
}


def enq() :
    print("\nIs it :\n1) 5'-3'\n2) 3'-5'")
    while True :
        c2 = input('Enter your choice (1 or 2): ')
        if c2 in ['1','2'] : break
        print('Invalid choice!')
    seq = input('\nEnter your sequence (without any spaces or dashes) (eg - atagtccga): ').upper()
    return c2, seq

def complementary(c1, seq):
    if c1 == '1' :
        comp = seq.translate(seq.maketrans('ATGC', 'TACG'))
    elif c1 == '2' :
        comp = seq.translate(seq.maketrans('AUGC', 'UACG'))
    return comp

def format(c2, seq, comp) :
    if c2 == '1' :
        seq = f"5'-{seq}-3'"
        comp = f"3'-{comp}-5'"
    elif c2 == '2' :
        seq = f"3'-{seq}-5'"
        comp = f"5'-{comp}-3'"
    return seq, comp

def c_strand(c1, c2, seq) :
    comp = complementary(c1, seq)
    seq, comp = format(c2, seq, comp)
    print(f'\nYour strand : {seq}')
    print(f'Complementary strand : {comp}')
    return

def translation(seq, mrna) :
    codon_list = [(mrna[i:i+3]) for i in range(0, len(mrna), 3)]
    for i, codon in enumerate(codon_list) :
        codon_list[i] = codons[codon]
    print(codon_list)
    acid = '-'.join(codon_list)
    if 'Met' in codon_list :
        codon_list = codon_list[codon_list.index('Met')+1:]
    if 'Stop' in codon_list :
        codon_list = codon_list[:codon_list.index('Stop')]
    acid_s = '-'.join(codon_list)
    comp = complementary(c1, seq)
    seq, comp = format(c2, seq, comp)
    print(f'\nYour strand : {seq}')
    print('Amino acid sequence :', acid)
    if acid_s != acid :
        print('Amino acid sequence (between start and stop codons):', acid_s)
    return


print('''What sequence do you have?
1) DNA
2) mRNA''')

while True :
    c1 = input('Enter your choice (1 or 2) : ')
    c2, seq = enq()
    match c1 :

        case '1' :
            print('\nWhat do you want to do? \n1) Make complementary strand\n2) Convert to mRNA (Transcription)\n3) Convert to amino acid sequence (Translation)')
            while True :
                match input('Enter your choice (1, 2 or 3) : ') :

                    case '1' :
                        c_strand(c1, c2, seq)
                        break

                    case '2' :
                        tmp = seq
                        if c2 == '2' :
                            tmp = complementary(c1, seq)
                        mrna = tmp.translate(tmp.maketrans('T', 'U'))
                        seq, mrna = format(c2, seq, mrna)
                        print(f'\nYour strand : {seq}')
                        print(f'mRNA strand : {mrna}')
                        break

                    case '3' :
                        tmp = seq
                        if c2 == '2' :
                            tmp = complementary(c1, seq)
                        mrna = tmp.translate(tmp.maketrans('T', 'U'))
                        translation(seq, mrna)
                        break
                    
                    case _ :
                        print('Invalid choice!')

            break

        case '2' :
            print('\nWhat do you want to do? \n1) Make complementary strand\n2) Convert to amino acid sequence (Translation)')
            while True :
                match input('Enter your choice (1 or 2) : ') :

                    case '1' :
                        c_strand(c1, c2, seq)
                        break

                    case '2':
                        mrna = seq
                        if c2 == '2' :
                            mrna = complementary(c1, seq)
                        translation(seq, mrna)
                        break

                    case _ :
                        print('Invalid choice!')
                
            break
        
        case _ :
            print('Invalid choice!')

print('\nDone!')