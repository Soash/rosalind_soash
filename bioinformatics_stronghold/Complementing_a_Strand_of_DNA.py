file = open('rosalind_revc.txt', 'r')

dna = file.read().strip()
nbase = dict(zip('ACGT', 'TGCA'))

file = open('rosalind_revc_answer.txt', 'w')
rev = dna[::-1]
for x in rev:
    print(nbase[x], end='')
    file.write(nbase[x])

file.close()

