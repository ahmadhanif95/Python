#if else
a = int(input("enter your age"))
if a>=14:
    print("Your game starts now")
else:
    print("your age is less than 15")

x=19
if x>18:
    pass

#exercide 
print("Guess the number to win the game")
win_no=10
a=int(input("enter the number"))
if win_no==a:
    print("you win the game")
else:
    if win_no>a:
        print("The number you enter is too low")
    else:
        print("the number you enter is too high")
 # and or operators
 # 
 
a1 = int(input("enter your age"))
b1 =input("Enter your name")
if b1=="ahmad" and a1==20: # and use mean if one condition flase over all false
    print("you are not absent")
else:
    print("you are absent")

a2 = int(input("enter your age"))
b2 =input("Enter your name")
if b2=="ahmad" or a2==20: # and use mean if one condition flase over all false
    print("you are not absent")
else:
    print("you are absent")

x=input("Enter your name")
y=int(input("enter your age"))
if x[0]=='a'or x[0]=='A' and y>10:
    print("you can watch the movie")
else:
    print("you canot watch the movie")

age=int(input("enter your age"))
if age>0 and age<3:
    print("Ticket is free")
elif age>3 and age<6:
    print("your ticket is half")
else:
    print("your ticket is full")

#in keyword if with in use in loops data structures or many uses
name="ahmad"
if 'a' in name:
    print("a is present in name")
else:
    print("not present in name")

# check empty or not
name="abc"
if name: #true if have any thing in the string
    print("code")
else:
    print("empty")
nam=input("enter your name")
if nam: #true if have any thing in the string
    print(f"code with {nam}")
else:
    print("empty")

