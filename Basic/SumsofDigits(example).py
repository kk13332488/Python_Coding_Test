import sys
sys.stdin=open('SumofDigits.txt', 'r')
N = int(input())
a = list(map(int, input().split()))

# case1
# def digit_sum(x):
#     sum=0
#     while x > 0:
#         sum+=x%10
#         x=x//10
#     return sum

# case2
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum
max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)