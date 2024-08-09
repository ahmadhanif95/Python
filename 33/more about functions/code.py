# enumerate function
nam=['a','b','c','d']
pos=0
for name in nam:
    print(f"{pos}--->{name}")
    pos+=1

for pos,name in enumerate(nam):
    print(f"{pos}--->{name}")

def find(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos

n=['a','b','ca','d']
print(find(n,'ca'))

# map function 
# function that return a number of square
def s(a):
    return a**2
[s(1),s(2),s(3)]
no=[1,2,3,4,5]
sq=list(map(lambda a:a**2,no))
print(sq)

n=['a','b','ca','d']
lens = map(len,n) # map is iterable we run loop on map 
for i in lens:
    print(i)

#filter ffunctions







