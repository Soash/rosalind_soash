file = open('rosalind_dna.txt','r')

dna = file.read()
A = dna.count("A")
C = dna.count("C")
G = dna.count("G")
T = dna.count("T")
print(A,C,G,T)

file = open('rosalind_dna_answer.txt','w')
file.write(str(A)+' '+str(C)+' '+str(G)+' '+str(T))

file.close()

