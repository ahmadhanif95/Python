sq=[]
for i in range(1,11):
    sq.append(i**2)
print(sq)
#list comprehension
sq1=[i**2 for i in range(1,11)]
print(sq1)
a=[-1 for i in range(1,11)]
print(a)

l=['ahmad','boll','play']
l1=[]
for i in l:
    i.append(l[0])
print(l1)

l2=[i[0] for i in l]

def rev(l):
    return [name[::-1] for name in l]

print(rev(l))

