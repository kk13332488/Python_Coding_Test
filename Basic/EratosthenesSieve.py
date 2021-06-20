import sys
sys.stdin=open('EratosthenesSieve.txt', 'r')
N = int(input())

Prm_num = []

for i in range(1,N+1):
    Divisor = []
    for j in range(1, i):
        if i%j == 0:
            Divisor.append(j)
    if len(Divisor) == 1:
        if Divisor[0] == 1:
            Prm_num.append(i)

print(len(Prm_num))




