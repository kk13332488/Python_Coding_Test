import sys
# sys.stdin=open('ReversedPrmNum.txt', 'r')
N = int(input())
Num_list = list(map(int, input().split()))

def reverse(x):
    length = len(list(str(x)))
    for i in range(length):
        if x//10 == x/10:
            x = x//10
        else:
            break

    x = list(str(x))
    result = ''
    for i in range(len(x)-1, -1, -1):
        result += x[i]

    result = int(result)

    return result

def isPrime(x):
    if x == 1:
        return -1

    cnt = 0
    for i in range(2,x):
        if x%i == 0:
            cnt += 1

    if cnt == 0:
        return 1
    else:
        return -1


for i in range(N):
    Reversed_num = reverse(Num_list[i])
    Result = isPrime(Reversed_num)
    if Result == 1:
        print(Reversed_num, end = ' ')






