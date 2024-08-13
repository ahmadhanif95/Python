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
#we can itertae map and filter one time either tuples we can iterate many times

no=[1,2,3,4,5,6,7,8,9]
print(tuple(filter(lambda a:a%2==0,no)))

ne=[i for i in no if i%2==0]
print(ne)

#iterator or iterables
#tuples string --> iterables
a=iter(no)
print(next(a))

#iterator
sq=map(lambda a:a**2,no)
print(next(sq))
print(next(no)) #error list is not iterator

#zip functions
u=['u1','u2','u3']
name=['ahmad','ali','moiz']
print(list(zip(u,name)))

u=['u1','u2']
name=['ahmad','ali','moiz'] #it will zip till ali

# * operator with zip

l=[(1,2),(3,4),(5,6),(7,8)]
l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))
new_list=[]
for pair in zip(l1,l2):
    new_list.append(max(pair))

#eexercise:

def avg(*args):
    avg=[]
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg
l=[[1,2,3,4],[5,6,4,3],[2,4,7,8]]
print(avg(l))

#any all function
n1=[2,4,6,8,10]
e=[]
for num in n1:
    e.append(num%2==0)
 
# any and all practice
print(all([num%2==0 for num in n1]))

# min max

#in advance data stucture
def func(item):
    return len(item)

name=['ahmad','ali','arsalan']
print(max(name,key=func))

s={
   'ali': {'score':90,'age':4},
    'ahmad':{'score':100,'age':5}
}
max(s,key=lambda item:s[item]['score'])
f=('b','g','a')
#sort function will not sort the tuples
sorted(f)
print(f) #sorted function will not return tuple it will return list
s1={
   {'score':90,'age':4},
   {'score':100,'age':5}
}
sorted(s1, key lambda = d:d['age'] , reverse=True)
sorted(s1, key lambda = d:d['age'] )





