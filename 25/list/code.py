#data structures
#ordered collection of items
num=[1,2,3,4]
print(num)
word=['ahmad','hbsa','hfou']
mix=['6','hgds','2.5']
mix[0]='two'
mix[1:]='two'
print(mix)
word[1:]=['ahmad','hbsa','hfou']
print(word)
# how to add items in the list
fruits=['grapes','apple']
fruits.append('mango')
fruits.insert(1,"gro")
fruits.insert(10,"gro")
print(fruits)
fru=[]
fru.append('mango')
print(fru)
fruits2=['kpo','iuf']
frui=fruits+fruits2
fruits.extend(fruits2)
fruits.append(fruits2)

# pop method
fruits.pop() #(1it will delete at first position) 
print(fruits)
del fruits[1] # it will also delete its operator
fruits.remove("apple") #it wwill find in the list and then delete it
#if i pass which is not in list it will give me value error 
# if 2 same number or words are present in the list and call delete operation it will remove first and second remoain same

# in keyword
fruits=['grapes','apple']
if 'apple' in fruits:
    print("present")
else:
    print("absent")

ruits=['grapes','apple']
ruits.count()
ruits.sort()
print(ruits)

no=[5,9,7,85,6,4,2,7]
no.sort()
print(no)
no1=[5,9,7,85,6,4,2,7]
print(sorted(no1))
no.clear()#delete the list
print(no)
a=no.copy()

#is vs ==
#list compare
fruits0=['grapes','apple']
fruits1=['grapes','apple']
fruits2=['grapes','apple',"banana"]
print(fruits1==fruits2)
print(fruits1==fruits0)
print(fruits1 is fruits2)
#joint method
user=['ahmad','24']
print(','.join(user)) 

#list vs array
# orderd collection of items c c++ java store only one data type
#list store any data very flexible
#python array fix data type
# javascript array store any thing like python list its flexible
#numpy arrays for calculations binding with c libraries
#performance is very fast
#c is very fast progemming language


#stings vs list string are imutable  while list is mutable
s="strong"
l=[1,2,3,4]
l.append('abc')


#looping in the list

l=[1,2,3,4]
for i in l:
    print(i)

#while loop

i=0
while i<len(l):
    print(l[i])
    i=i+1


#list inside list

mat=[[1,2,3],[4,5,6],[7,8,9]]
print(mat[0])
print([0][2])
for sublist in mat:
    for i in sublist:
        print(i)

#type function
s="string"
print(type(s))

print(type(mat))

#genrate list with rnage function
no=list(range(1,11))
print(no)

#pop method
print(no.pop())#it will return 10  because data will not lost
pop_item=no.pop()
print(no)

#index method
print(no.index(1)) #it will tell me the position of 1
#index will search by default 0 th position

print(no.index(1,5)) #it will search after 5 the position

print(no.index(1,0,20)) # mean we will stop seaching at 20 th positon

#lis pass to a function
def neg(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
neg(no)


# examples exercises:
#def function as input list consist of number and return no of square

def squ(s):
    squa=[]
    for i in s:
        squa.append(i**2)
    return squa
la=list(range(1,11))
print(squ(la))

# exercise 2
#fucntion take as list reurn its reverse
def rev(l):
    l.reverse()
    return l
def reve(l):
    return l[::-1]

def rever(l):
    r=[]
    for i in range(len(l)):
       pop_item = l.pop()
       r.append(pop_item)
    return r


# as input take list list consist of words
# every sting is reverse 
def rev_ele(l):
    ele=[]
    for i in l:
        ele.append(i[::-1])
    return ele


#exercise list in which seprate out odd even number
l=[1,2,3,4,5,6,7,8]

def filter_odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[odd,even]
    return output

filter_odd_even(l)

#exercise find common number from l1 and l2

def common_num(l1,l2):
    out=[]
    for i in l1:
        if i in l2:
            out.append(i)
    return out

a=[1,2,3,4,5,6,7]
b=[1,2,3,8,9,7,5]
commom_num(a,b)

#min max function

print(max(a))
print(min(a))

# find sublist in list
def sublist(l):
    count=0
    for i in l:
        if type(i)==list:
            count+1
    return count

a=[1,2,[3,4],4,[6,7],8]
sublist(a)



