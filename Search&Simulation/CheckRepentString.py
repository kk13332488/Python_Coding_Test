import sys
# sys.stdin=open('CheckRepentString.txt', 'r')
N = int(input())
WordList = []
for i in range(N):
    WordList.append(input().lower())
ReversedWord = []

for i in range(N):
    tmp = ""
    for j in range(len(WordList[i])-1, -1, -1):
            tmp += WordList[i][j]
    ReversedWord.append(tmp)

for i in range(N):
    if WordList[i] == ReversedWord[i]:
         print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))
