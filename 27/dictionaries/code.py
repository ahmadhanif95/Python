#if you want to colled data from user
l=[name,ahmad,age,24]
 # we use dictionaries

user = {'name':"ahmad","age":24}
print(user)
print(type(user))
print(user['name'])
#new line
user = dict(name='ahmad',age=24)
# there will be no indexing in dictionaries
print(user['name'])
print(user['age'])
#we story any thing in dic number list stings dic
user_info = {
    'name': "ahmad",
    'age': 24,
    'courses': ['oop','dsa'],
}
print(user_info['courses'])
user_info2 = {}
user_info2['name']='ahmad'
user_info['age']=23
# check if column exist in dictionary
if 'name 'in user_info:
    print("present")
else:
    print("not present")

#check if value exist in dict
if 'ahmad' in user_info.values:
    print("present")
else:
    print("not present")
#if you want to check complete list
if ['oop','dsa'] in user_info.values:
    print("present")
else:
    print("not present")


#looping in dictionariyoes
for i in user_info:
    print(i) # it will print all keys

for i in user_info.values:
    print(i) # it will print all values in dict


user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

for i in user_info:
    print(user_info[i]) # it will print all values

#item method

user_items=user_info.items()
print(user_items)
print(type(user_items))
#it will return list and there are too many tuples in it
#tuple unpacking
for key,values in user_info.items():
    print(f"key is {key} and value is {value}")
#in keyword and iteratt to check complete ions
# add delete data from dictionaries
user_info['fav_music'] = ['s1','s2']
print(user_info)

#pop method

#pop method delte from dict
pop_item=user_info.pop('fav_music') #pass atleast 1 aargument
print(f"pop item is {pop_item}")

pop_tiem=user_info.popitem()
print(f"pop item is {pop_item}")
print(f"pop item is {type(pop_item)}")

#update method

more_info={'state':'pakistan','hobbies':['coding','studing','teaching','pets']}
user_info.update(more_info)
print(user_info)
user_info.update({})#it means that there will be no data update previous data wll not delete

#fromkeys get copy clear method
#d={'name':'unknown','age':'unknown'}
d=dict.fromkeys(['name','age','height'],'unknown')
#we should also write tuple instead of list
e=dict.fromkeys(('name','age','height'),'unknown')
f=dict.fromkeys('abcd','unknown')
#abcd will become seprate key
g=dict.fromkeys(range(1,11),'unknown')
h=dict.fromkeys(['name','age','height'],['unknown','unknown','unknown'])
print(d)
print(d['names']) #key error

#how to use get method
print(d.get('name'))
print(d.get('names')) #it will return none no key error
#better to acess keys
if d.get('name'):
    print('present')
else:
    print("absent")
d1=d.copy()
d.clear()
print(d) #dict will be empty
print(d1)

d1=d
print(d1.popitem())
print(d) #because both are equal it will pop both dictionaries

#check both are dierrent or same dict
print(d1 is d) # ==

# more about get()

print(user_info.get('names','not found!'))


user = {'name':"ahmad","age":24,'age':36}

print(user)#value override


#exersie function take number and find cube in dic
dict={}
def cube(n):
    for i in range(n):
        dic={i:i**3}
        dict.update(dic)
cube(3)
print(dict)


# word counter using dict
d={'a':1,'b':3}

def counter(a):
    count={}
    for i in a:
        count[i]=a.count(i)
    return count
print(counter('ahmaddddd'))

#exercise
disco={}
name=input('enter your name')
age=input('enter you age')
education=input('enter your specialization streams').split(',')
disco['name']=name
disco['age']=age
disco['education']=education








