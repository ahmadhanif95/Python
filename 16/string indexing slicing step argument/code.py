#string indexing
lan='python'
print(lan[2])
# python 012345    -6-5-4-3-2-1
#string slicing
#to print one or more character
#[stratr argument:end argument]

print(lan[0:2])
print(lan[2:4])
print(lan[3:6])
print(lan[-3:6])
print(lan[:])
print(lan[1:])
print(lan[:-1])
print(lan[:2])

#step argument
print('ahmad'[2:5])
print('ahmad'[0::2])
print('ahmad'[2:5:1])#step of one difference
print('ahmad'[5::-1]) # it means that to move back from last to end
print('ahmad'[-1::-1]) #the string is reverse
print('ahmad'[::-1]) #by default its going to reverse
# string Methods
name = "ahmad ali arsalan"
#length function
print(len(name))

# lowwer method
print(name.lower())

# upper
print(name.upper())

#title
print(name.title())
 #count
print(name.count('a'))



