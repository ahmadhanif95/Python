#center method
name="ahmad"
print(len(name))
print(name.center(11,"*"))
#practice
a = input("enter name")
print(name.center(len(name)+8,"*"))
# strings are immputable
string="string"
print(string[1])
string[1]="T" # it will not change its mean it is immutable
b=string.replace('t','T') 
b=string.replace('t','T',1)
b=string.replace('t','T',2)# we change it and replace and 
#store into new variable so but we dont edit into string varible
#  
print(b)

# assignmemnt operators
name="ahmad"
name=name+"it"
name+="ahmad"
print(name)
# == -= *=

