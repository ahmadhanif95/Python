name='ahmadali'
print(len(name))
def add_two(a,b):
    return a+b
add_two(5,5) 
 a = int(input("enter 1 num"))
 b = int(input("enter 2 num"))
add_two(a,b) 
 # rerutn vs print
def add_two(a,b,c):
    print(a+b+c)

def add_two(nam):
    return nam[-1]

def odd_even(num):
   if num%2==0:
      return "even"
   else:
      return "odd"
print(odd_even(10))

def odd_even(num):
   if num%2==0:
      return "even"
   return "odd"
print(odd_even(10))


def iseven(num):
   if num%2==0:
      return True
   else:
      return False
   
iseven(9)

def iseven(num):
   return num%2==0

def greater(a,b):
   if a>b:
      return a
   else:
      return b

num1 = int(input("enter the number 1"))
num2 = int(input("enter the number 2"))
print(f"greater number is : {greater(num1,num2)}")

def greatest(a,b,c):
   if a>b and a>c:
      return a
   elif b>a and b>c:
      return b
   else:
      return c

num1 = int(input("enter the number 1"))
num2 = int(input("enter the number 2"))
num3 = int(input("enter the number 3"))
print(f"greater number is : {greatest(num1,num2,num3)}")

# inside function
def new(a,b,c):
   bigger = greater(a,b)
   #return greater(greater(a,b),c)
   return greater(bigger,c)

# palindrome exerecise practice
def word(name):
   reverse=word[::-1]
   if word==reverse:
      return True
   else:
      return False
#fibonacci series
# 0 1 1 2 3 5 8 13 21 34
def num(no):
   a=0
   b=1
   if no ==1:
      print(a)
   elif no == 2:
      print(a,b)
   else:
      print(a,b ,end=" ")
      for i in range(no-2):
      c= a+b
      a=b
      b=c
      print(b,end=" ")


#def user(a,b='unknown',c=None):
def user(a,b,c=None):
   print(f"a{a}")
   print(f"b:{b}")
   print(f"c:{c}") 

user(1,2,3)  
#user(1,ali)

#variable scope
x=10
def dunc():
   #global x ver less in life time issue in code maintaing
   # golbal variable canot change in local funciton
   x=9
   return x
def dun():
   print(x)
print(x)
print(dunc())

      