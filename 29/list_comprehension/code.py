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

# if else

no = list(range(1,11))
even=[i for i in no if i%2==0]
odd=[i for i in range(1,11) if i%2!=0]

def no_to_string(l):
    return[str(i) for i in l if type(i)==int or type(i)==float]
print(no_to_string([True,False,[1,2,3],1,1.0,3]))

no = list(range(1,11))
new_list = []
for i in no:
    if i%2==0:
        new_list.append(i*i)
    else:
        new_list.append(-1*i)
print(new_list)
new_list2=[i*2 if i%2==0 else -1*i for i in no]
print(new_list2)

#nested list
nest=[[i for i in range(1,5)]for j in range(10)]
print(nest)


