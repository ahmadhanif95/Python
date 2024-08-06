sq={num:num**2 for num in range(1,11)}
squ = {f"square of {num} is":num**2 for num in range(1,11)}
for k,v in squ.items():
    print(f"{k}:{v}")

string="ahmad"
count={char:string.count(char) for char in string}
print(count)

odd_even={i:('even' if i %2==0 else 'odd')for i in range(1,11)}
print(odd_even)

#set comprehension
s={k**2 for k in range(1,11)}
print(s)  #there will be no order of set and dictionary




