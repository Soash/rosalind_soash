file = open('rosalind_fib.txt', 'r')

data = file.read().split()
months, offsprings = int(data[0]), int(data[1])

childs, parents, total = 1, 1, 0

for i in range(1, months+1):
    if i == 1:
        childs = parents*1
    else:
        childs = parents*offsprings
    parents = total

    total = parents+childs
    
    # print(i,'month : '+'childs = ',childs,'parents = ',parents,'total = ',total)
print(total)

file = open('rosalind_fib_answer.txt', 'w')
file.write(str(total))

file.close()

