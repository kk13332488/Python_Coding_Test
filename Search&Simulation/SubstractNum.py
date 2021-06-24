import sys
sys.stdin=open('SubstractNum.txt', 'r')
string = input()

cnt = 0
num = ""
for i in range(len(string)):
    if 48 <= ord(string[i]) <= 57:
        cnt += int(string[i])
        if cnt != 0:
            num+=(string[i])

num = int(num)
divisor = 0
for i in range(1,num+1):
    if num%i == 0:
        divisor += 1

print(num)
print(divisor)


