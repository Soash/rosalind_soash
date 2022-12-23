file = open('rosalind_rna.txt', 'r')

dna = file.read().strip()
rna = dna.replace('T', 'U')
print(rna)

file = open('rosalind_rna_answer.txt', 'w')
file.write(rna)

file.close()

