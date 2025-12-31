# Write a program to perform insertion sort on a given array of any length
import datetime
import random

l = [random.randint(1, 100) for _ in range(10000)]
#l=[3,2,6,5,1,9,6,7,14,12,11,20]
print(datetime.datetime.now())
while True:
    j=0
    for i, v in enumerate(l):
        if len(l)-1==i:
            continue
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            j=j+1
            #print(i,i+1,l[i],l[i+1],l,"===", j)
    if j == 0:
        #print("break")
        break
print(datetime.datetime.now())
#print(l)
