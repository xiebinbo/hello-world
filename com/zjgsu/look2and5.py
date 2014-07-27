'''
Created on 2014年7月3日

@author: pliro
'''
L= [2,3,4,5,6,7,8,9]
m=0
n=0
for i in L:
    t=i
    while t%2==0:
        t/=2
        m+=1
    while t%5==0:
        t/=5
        n+=1
if m>n:
    print (n)
else:
    print (m)