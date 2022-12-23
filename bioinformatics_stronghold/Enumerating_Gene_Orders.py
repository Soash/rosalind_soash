from itertools import permutations

file = open('rosalind_perm.txt', 'r')
x = file.read()

fact = 1
nums = []
for i in range(1,int(x)+1):
    fact*=i
    nums.append(str(i))

file = open('rosalind_perm_answer.txt', 'w')
file.write(str(fact)+'\n')
print(fact)
for p in permutations(nums):
    x = ' '.join(p)
    file.write(x+'\n')
    print(x)

file.close()

