# decorators very important many peoples skip this topic
# complete under stnading of functions
#first class functions / closures
#then move on to decorators

def sq(a):
    return a**2
s=sq
print(s(8))
print(s.__name__)
print(sq.__name__)
print(s)
print(sq)


# in this we learn how to take function as argument
def my_fun(func,l):
    new_l=[]
    for item in l:
        new_l.append(func(item))
    return new_l

l=[1,2,3,4,5]
print(my_fun(sq,l))

#function returning function
def out():
    def inner():
        print("inside innner function")
    return inner
a=out()
def f2(msg):
    def f_inner():
        print(f"message is {msg}")
    return f_inner

b=f2("hello i am ahmad")
b()

#closures practice
def p(x):
    def cal(n):
        return n**x
    return cal
cube=p(3)
cube(5)
sq=p(2)
sq(2)

from functools import wraps

# decorators
def decorator(any_func):
    @wraps(any_func)
    def wrapper(*args,**kwargs):
        print("this is awesome")
        """this is wrapper function"""
        return any_func(*args,**kwargs) #then it will return values because we never return values just return function now our function work properly for any function
    return wrapper
# @ use for decorator



@decorator #it will enhance function fi functionality
def fi(a):
    print(f"this is function 1 with valuse argument {a}")

def f3():
    print("this is function 3")

fi(9)

var=decorator(fi)
print(var())
#this is awesome
fi()
f3()
@decorator 
def add(a,b):
    """this is add function"""
    return a+b
add(3,3) # it will not print
print(add(3,3)) #it will give none no give sum why because we never return to any functions
#now there will be no problem
add(3,3)


# problem docstring
"""this is wrapper function"""
print(add.__doc__) #it will give wrapper function
print(add.__name__) # it will print wrapper function name
#its a problem 
#so handling this prolem we need to import module
from functools import wraps
# so add this library into it it will resolve out issue and at upper we add  a warpper



#practice
from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper
@print_function_data
def add(a,b):
    '''this function will add 2 values and return sum'''
    return a+b
print(add(4,5))

#second practice
from functools import wraps
import time

def cal_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"executing ... {function.__name.__}")
        t1=time.time()
        ret=function(*args,**kwargs)
        t2=time.time()
        total=t2-t1
        print(f"This fucntion take {total} seconds time to run")
        return ret
    return wrapper
@cal_time
def sq(n):
    return [i**3 for i in range (1,n+1)]
print(sq(1000))

#practice
from functools import wraps
def int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        data_types=[]
        for arg in args:
            data_types.appent(type(args==int))
        if all(data_types):
            return function(*args,**kwargs)
        else:
            print("invalid arguments")
    return wrapper
@int_allow
def add_all(*args):
    total=0
    for i in args:
        total=total+i
    return total
print(add_all(1,2,3,4,5,6))
print(add_all(1,2,3,4,[5,6],9))


#decorator with arguments
from functools import wraps
def only_dtype_allow(data_types):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            data_types=[]
            for arg in args:
                data_types.appent(type(args==data_types))
            if all(data_types):
                return function(*args,**kwargs)
            else:
                print("invalid arguments")
        return wrapper
    return decorator
@only_dtype_allow(str)
def string_join(*args):
    string=''
    for i in args:
        string+=i
    return string

string_join('ahmad',' is out side')