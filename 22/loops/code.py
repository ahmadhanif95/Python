i=0
while i<10:
    print("hello world")
    i=i+1

total=0
i=0
while i<10:
    total=total+i #total+=i
    i=i+1 #i+=1

#exercise
a=input("enter the number")
b=int(a)
total=0
i=0
while i<b:
    total+=i
    i+=1
#exercise
x=input("enter the number")
total=0
y=len(x)
i=0
while i<y:
    total+=int(x[i])
    i+=1
print(total)
#exercise
name=input("enter your full name")
i=0
while i<len(name):
    print(f"{name[i]}:{name.count(name[i])}")
    i=i+1
# infinite loop

i=0
while i<10:
    print("gaikhg")
    #press ctrl+c to  infinite loop
#
while True:
    print("hello")

# boolean Ture False
#for loops
#for loop with range function
for i in range(10): #(1,11)
    print(f"hello{i}")

total =0
for i in range(1,21):
    totral+=i
print(total)

a=input("enter the number")
total =0
for i in range(len(a)):
    total+=int(a[i])
print(total)
name=input("enter name")
for i in range(len(name)):
    print(f"{name[i]}:{name.count(name[i])}")
