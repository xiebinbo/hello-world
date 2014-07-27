'''
Created on 2014年7月3日

@author: pliro
'''
import math
L=[]
for j in range(2,100):
    flag = 1
    for  m in range(2,int(math.sqrt(j))+1):
        if j%m == 0:
            flag = 0
    if flag == 1:
        L.append(j)
print(L)    
print (' '.join(str(i) for i in L))