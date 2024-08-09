# lambda expression

def add(a,b):
    return a+b

# use with builtin functions
 
multiply = lambda a,b :a*b
print(multiply(2,3))

a = lambda i : i%2==0
ls= lambda s : s[-1]
print(ls['ahmad'])
def dun(s):
    if len(s)>5:
        return True
    else:
        return False
dun1=lambda s: True if len(s)>5 else False
print(dun('abcdefgh'))











