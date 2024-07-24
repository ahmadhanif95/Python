exam=('a','b','c')
# tuples are imutaaable
#tuples are faster beter than list
print(example[:2])
for i in exam:
    print(i)

#list in tuple
exe=('a',['b','c'],'d')
exe[1].pop()
exe[1].append('hello how are you')
print(exe)
ex=(1,2,3,4)
print(min(ex))
print(max(ex))

#function returning 2 values
def fun(a,b):
    add=int(a)+int(b)
    mul=a*b
    return add,mul
print(fun(2,3))
#it will give me tuple

num=tuple(range(1,20))
print(num)
a=list((1,2,3,4,5,6,7,8,9))
b=str((1,2,3,4,5,6,7,8,9))
print(a)
print(type(a),type(b))