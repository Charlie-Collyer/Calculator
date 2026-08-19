#Define Variables
num1 = float(0.0)
num2 = float(0.0)
operation = str("")

#Define Functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

#Main Program
#Request user input for numbers and operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Provide user with operation options and request input for operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter operation (1/2/3/4): ")

#Perform the selected operation and display the result
#Reject invalid operations and prompt the user to enter a valid operation
while True:
    if operation == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
        break
    elif operation == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
        break
    elif operation == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
        break
    elif operation == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
        break
    else:
        operation = input("You entered an invalid operation. Enter operation (1/2/3/4): ")