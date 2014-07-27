'''
Created on 2014年7月3日

@author: pliro
'''
L = [3,4,6,8,5]
L.sort()
length = len(L)
if length%2 == 0:
    print ((L[length/2]+L[length/2-1])/2.0)
else:
    print (L[int(length/2)])