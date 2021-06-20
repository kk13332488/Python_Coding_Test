import sys
import numpy as np
sys.stdin=open('SumofDigits.txt', 'r')
N = int(input())
a = list(map(int, input().split()))

sums = []
def digit_sum(x):
    x = list(str(x))
    result = 0
    for num in x:
        num = int(num)
        result += num
    sums.append(result)

for num in a:
    digit_sum(num)

Max_sum = 0
for i in range(N):
    if sums[i] > Max_sum:
        Max_sum = sums[i]

for i in range(N):
    if sums[i] == Max_sum:
        print(a[i])






