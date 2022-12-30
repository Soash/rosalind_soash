file = open('rosalind_iprb.txt', 'r')
data = file.read().split()

k, m, n = int(data[0]), int(data[1]), int(data[2])
t = k+m+n
x = t-1
a = (m/t)*((m-1)/x)*0.25
b = (m/t)*(n/x)*0.50
c = (n/t)*(m/x)*0.50
d = (n/t)*((n-1)/x)
problty = 1 - (a+b+c+d)

print('{:.5f}'.format(problty))

file = open('rosalind_iprb_answer.txt', 'w')
file.write('{:.5f}'.format(problty))

file.close()
