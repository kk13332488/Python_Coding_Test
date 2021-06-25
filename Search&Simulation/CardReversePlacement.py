import sys
# sys.stdin=open('CardReversePlacement.txt', 'r')
cardlist = [i for i in range(1,21)]

for i in range(10):
    emptylist = []
    start, end = map(int, input().split())
    tmp = cardlist[start-1:end]
    for i in range(len(tmp)-1, -1, -1):
        emptylist.append(tmp[i])
    cardlist[start-1:end] = emptylist

for i in range(20):
    print(cardlist[i], end=' ')

