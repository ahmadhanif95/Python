# break and continue
for i in range(10):
    if i==5:
        break
    print(i)
#continue

for i in range(10):
    if i==5:
        continue
    print(i)

#game
win=50
guess=1
num=int(input("guess the number"))
over=False
while not over:
    if win==num:
        print(f"You win the same after {guess} times")
    else:
        if num<win:
            print("too low guess the number again")
            guess+=1
            num=int(input("guess the number"))
        else:
            print("too high guess the number again")
            guess+=1
            num=int(input("guess the number"))


# dry principle of coding
#game
import random
win=random.randint(1,100)
guess=1
over=False
while not over:
    num=int(input("guess the number"))
    if win==num:
        print(f"You win the same after {guess} times")
    else:
        if num<win:
            print("too low guess the number again")
        else:
            print("too high guess the number again")    
        guess+=1
        continue

# step argument in range
for i in range(1,11,2):
    print(i)

for i in range (10,0,-1):
    print(i)

# for loop and string
name="ahmad ali"
for i in range(len(name)):
    print(name[i])

for i in name:
    print(i)

#exercise
num=input("eneter numbers")
total=0
for i in num:
    total+=int(i)