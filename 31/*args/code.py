#make fexilable functions
def tot(a,b):
    return a+b
print(tot(1,2,3,4,5))

def all(*args):
    print(args)
    print(type(args))
    t=0
    for i in args:
        t+=i
    return t
all(1,2,3,4,5,6,7,8)
#it will take tuples as argument

#args  with normal parameter

def mul(num,*args):
    mul=1
    print(num)
    print(args)
    for i in args:
        multiply*=i
    return multiply
print(mul(2,2,3,4,5))
print(mul())             #it will give error
# if we write args first then write other varibale 
#its wrong because all varible pass into args num is empty and give you error

 # use of args as arguments
def mul(num,*args):
    mul=1
    print(num)
    print(args)
    for i in args:
        multiply*=i
    return multiply
l=[2,2,3,4,5]
print(mul(*l))  #we write * to unpack list elements

#exercise
def power(num,*args):

    if args:
        return [i**num for i in args]
    else:
        return "didnot pass any args"
l1=[1,2,3,4,5]
print(power(2,*l1))

#*kwargs as parameter keyword arguments

def fun(**kwargs):
    print(**kwargs)
    print(type(**kwargs))
    for i,j in kwargs.items():
        print(f"{i}:::{j}")
fun(f='ahmad',l='ali')

def fun(nam,**kwargs):
    print(nam)
    print(**kwargs)
    print(type(**kwargs))
    for i,j in kwargs.items():
        print(f"{i}:::{j}")
fun('ali',f='ahmad',l='ali')

#dict unpacking
d={'nam':'ali','age':23}

def fun(nam,**kwargs):
    print(nam)
    print(**kwargs)
    print(type(**kwargs))
    for i,j in kwargs.items():
        print(f"{i}:::{j}")
d={'nam':'ali','age':23}
fun('ali',**d)


# deafult params params args kwargs
# PADK
def fun(name,*args,l_name='unknown',**kwargs):
    print()

#def fun input list return list return list in which first letter of string is capital
def cap(a,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [i[::-1].title() for i in a]
    else:
        return [i.title()for i in l]

n=['ali','ahmad']
print(cap(n,reverse_str=True))








