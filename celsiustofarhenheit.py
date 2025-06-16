import math
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error: Cannot divide by zero"
#     return x / y

# print("Simple Calculator")
# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# # Get numbers from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Perform operation
# if choice == '1':
#     print("Result:", add(num1, num2))
# elif choice == '2':
#     print("Result:", subtract(num1, num2))
# elif choice == '3':
#     print("Result:", multiply(num1, num2))
# elif choice == '4':
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid input")
def positivenegative(number):

    if number > 0:
        return "positive"
    elif number< 0:
        return "negative"
    else:
        return "zero"

def odd_even(number):
    if number % 2==0:
        return "even"
    else: 
        return "odd"

def factorial(number):
    return math.factorial(number)
        
print("1. positive negative")
print("2. even odd")
print("3.factorial")
    
choice = input("Enter choice (1/2/3): ")
number =int(input("enter your number"))
if choice == '1':
    print("Result:", positivenegative(number))
elif choice == '2':
    print("Result:", odd_even(number))
elif choice == '3':
    print("Result:", factorial(number))
else:
    print("Invalid input")



# def fibonacci_generator(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# # Example usage
# print(list(fibonacci_generator(10)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
