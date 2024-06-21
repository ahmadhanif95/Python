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

    