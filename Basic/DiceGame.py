import sys
#sys.stdin=open('DiceGame.txt', 'r')

def Max_val(list_x):
    max = 0
    for i in range(len(list_x)):
        if list_x[i] > max:
            max = list_x[i]
    return max

N = int(input())
Res_list=[]

for i in range(N):
    res = list(map(int, input().split()))
    Res_list.append(res)

Award = []
for i in range(N):
    Nth_res = Res_list[i]
    cnt = 0
    tmp = 0
    num = 0
    for i in range(len(Nth_res)):
        if tmp == Nth_res[i]:
            cnt += 1
            num = Nth_res[i]
        tmp = Nth_res[i]
    if cnt == 2:
        money = 10000 + num * 1000
        Award.append(money)
    elif cnt == 1:
        money = 1000 + num * 100
        Award.append(money)
    else:
        max_num = Max_val(Res_list[i])
        money = max_num * 100
        Award.append(money)

print(Max_val(Award))



