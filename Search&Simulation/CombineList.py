import sys
#sys.stdin=open('CombineList.txt', 'r')
n1 = int(input())
list1 = list(map(int, input().split()))
n2 = int(input())
list2 = list(map(int, input().split()))

list_tmp = [0 for i in range(101)]
for i in list1:
    list_tmp[i] += 1
for i in list2:
    list_tmp[i] += 1

for i, x in enumerate(list_tmp):
    if x != 0:
        for j in range(x):
            print(i, end=' ')

