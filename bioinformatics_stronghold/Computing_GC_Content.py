file = open('rosalind_gc.txt', 'r')

x = file.read().split()

seq=''
id=[]
nbase=[]
for i in range(len(x)):

    if '>' in x[i]:
        nbase.append(seq)
        id.append(x[i])
        seq=''

    elif '>' not in x[i]:
        seq = seq+x[i]
        if i==len(x)-1:
            nbase.append(seq)
            nbase.remove('')

# print(id)
# print(nbase)

highest_gcc = 0
for i in range(len(id)):
    gc_ratio = (nbase[i].count('G')+nbase[i].count('C'))/len(nbase[i]) * 100

    if gc_ratio > highest_gcc:
        highest_gcc = gc_ratio
        highest_id = id[i]

print(highest_id[1:])
print('{:.6f}'.format(highest_gcc))

file = open('rosalind_gc_answer.txt', 'w')
file.write(highest_id[1:]+'\n{:.6f}'.format(highest_gcc))

file.close()

