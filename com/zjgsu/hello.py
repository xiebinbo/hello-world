'''
Created on 2014年5月31日

@author: pliro
'''
a={1:1,2:2,3:3}
b = []
for i in a.keys():
    b.append(str(i))
print(b)
print (','.join(b))