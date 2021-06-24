import sys
sys.stdin=open('ScoreCal.txt', 'r')
N = int(input())
scorelist = list(map(int, input().split()))
N += 1
scorelist.append(0)

cnt = 0
idx = -1
for i in range(0,N):
    if scorelist[i] == 0:
        num = i - idx - 1
        Sum = sum([i for i in range(num+1)])
        idx = i
        cnt += Sum

print(cnt)

