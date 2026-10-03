# Program to perform basic arithmetic operations and check the sign of the numbers

Number1 = int (input("Enter first number: "))
Number2 = int (input("Enter second number: "))
add = Number1 + Number2
subtract = Number1 - Number2
Multiply = Number1 * Number2
Division = Number1 / Number2
Percentage = (Number1 / Number2) * 100
print(f"The result of adding {Number1} and {Number2} is: {add}")
print(f"The result of subtraction is: {subtract}")
print(f"The result of multiplication is: {Multiply}")
print(f"The result of division is: {Division}")
print(f"The percentage of {Number1} relative to {Number2} is: {Percentage}")

if Number1 > 0 and Number2 > 0:
    print(f"\nThe entered numbers are positive")
elif Number1 < 0 and Number2 < 0:
    print(f"\nThe entered numbers are negative")
else:
    print(f"\nThe entered numbers have different signs")

# Program to check if the entered numbers are even or odd

if Number1%2 == 0 and Number2%2 == 0:
    print(f"\nThe entered numbers are even \n")
elif Number1%2 != 0 and Number2%2 != 0:
    print(f"\nThe entered numbers are odd \n")
elif Number1%2 == 0 and Number2%2 != 0:
    print(f"\nThe first number is even and the second number is odd")
else:
    print(f"\nThe first number is odd and the second number is even")

# Program to perfrom string concatenation and check the data type of the entered strings

String1 = str(input("\nEnter your name: "))
String2 = str(input("\nEnter your age: "))
print(f"\nHello {String1}, welcome to the program!" + f" - You are {String2} years old.")
print(type(String1))
print(type(String2))

# Program to convert the entered temperature from Celsius to Fahrenheit

Celsius = float(input("\nEnter temperature in Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
print(f"\nThe temperature in Fahrenheit is: {Fahrenheit}")
