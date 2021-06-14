import sys
import numpy as np
sys.stdin=open("RepresentValue.txt", "r")
N = int(input())
student = list(map(int, input().split()))

mean_score = round(np.sum(student)/N)

dev_student = []
for i in range(N):
    dev = abs(student[i] - mean_score)
    dev_student.append(dev)

idx_min = list(np.where(dev_student == np.min(dev_student)))[0] #must use slicing because the return value is tuple.

student_min = []
for i in idx_min:
    student_min.append(student[i])

min_max = list(np.where(student_min == np.max(student_min)))[0]

print(mean_score, idx_min[min_max[0]]+1)







