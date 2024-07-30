#set data type
# unorderd collection of unique data type
s=[1,2,3,4,5,6,7,8,9,9,9,] # means one item is not more than 1 time
#remove dublicate
s1=set(s) #it will remove all dublicate as per set 
print(s1)
#methos of set
s1.add(4)
print(s1)
s1.add(10)
s1.add(4)
s1.remove(3)
print(s1)
#wrtie those number whihc is in set
# discard method
s1.discard(100) #it will not give you error
print(s1.clear)
print(s1)
s2=s1.copy()
print(s2)
 # we dont store list dict in set
s={1,2.3,"ahmad"}
print(s)


for i in s:
    print(i)

if 'ahmad' in s:
    print("ahmad")
else:
    print("absent")

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8,9}
union = s1 | s2
print(union)
intersection = s1 & s2
print(intersection)

