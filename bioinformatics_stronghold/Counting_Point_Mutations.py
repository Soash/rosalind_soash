file = open('rosalind_hamm.txt', 'r')
seq = file.read().split()

hamming_distance = 0
for i in range(len(seq[0])):
    if seq[0][i] != seq[1][i]:
        hamming_distance+=1
print(hamming_distance)

file = open('rosalind_hamm_answer.txt', 'w')
file.write(str(hamming_distance))

file.close()

