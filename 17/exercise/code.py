name = input("enter your name: ")
rev = name[::-1]
print(f"reverse name is {rev}")

#2 enter the name and then enter the letter which is 
# case sensetive Ahmad if a is ounted in it so a have 
# 2 times present in data
namei,lette=input("enter the name and letter: ").split(",")
nam=namei.lower()
lett=lette.lower()
print(nam.count(lett))
