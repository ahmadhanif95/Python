#print("hello world my 'name' is ahmad")
# inputs from the user
print("*************Calculator****************")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result="Error Division by zero is not allowed"
else:
    result="Error Invalid operation"
print(f"Result is:{result}")
print("*************Thankyou for Using me****************")
