def to_rna(dna_strand):
    rna=[]
    for i in dna_strand:
        if i=='G':
            rna.append('C')
            print("blue")
        elif i=='C':
            rna.append('G')
        elif i=='T':
            rna.append('A')
        elif i=='A':
            rna.append('U')
        else:
            raise ValueError("Enter a correct DNA sequence")
    return ''.join(rna)

