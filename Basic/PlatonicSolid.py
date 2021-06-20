import sys
from scipy.stats import mode
import numpy as np

sys.stdin=open('PlatonicSolid.txt', 'r')
N, M = map(int, input().split())

Max = N+M
cnt = []
for i in range(N+M+1):
    cnt.append(0)

for i in range(1,N+1):
    for j in range(1,M+1):
        cnt[i+j] += 1

score = 0
Max_value = 0
for i in range(N+M+1):
    if cnt[i] > Max_value:
        Max_value = cnt[i]

for i in range(N+M+1):
    if cnt[i] == Max_value:
        print(i)







