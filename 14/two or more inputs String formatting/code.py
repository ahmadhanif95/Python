n=input('enter name')
a=input('entrer age')
name,age =input('enter name and age').split(",")
print(name)
print(age)
# string formatiiing
print("hello{} and your age is {}".format(name,age+4)) # py 3
print(f"hello {name} your age is {age+3}") #py 3.6
