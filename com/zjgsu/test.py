#===============================================================================
# s = "fsdgfahgflsdyhrldst"
# L=[]
# print(s)
# for c in s:
#     L.append(chr(97 + (ord(c) + 3 - 97) % 26))
#      
# print("".join(L))
#  
# a = '2008'
# print(int(a)+1)
#  
# for i in range(10):
#     print(i,end=' ')
#===============================================================================

#===============================================================================
# t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
# L = t.values()
# print(L)
# L = t.keys()
# print(L)
# print(t.items())
#===============================================================================
def _traverse(i,limit,cost):
    _limit=[]
    _cost=[]
    t=0
    for ele in limit[i:len(limit)]:
        _limit.append(ele)
    for ele in limit[0:i]:
        _limit.append(ele)
    
    for ele in cost[i:len(cost)]:
        _cost.append(ele)
    for ele in cost[0:i]:
        _cost.append(ele)    
    for ele in range(len(limit)):
        t=t+_limit[ele]-_cost[ele]
        if t<0:
            return -1
    if t>0:
        return i
        
limit = [3,4,5,6,7,8,9]
cost = [1,2,3,4,5,6,7]
r = 0 
r = _traverse(3,limit,cost)
print(r)    
            
        
           
        