# Program to perform basic arithmetic operations and check the sign of the numbers

Number1 = int (input("Enter first number: "))
Number2 = int (input("Enter second number: "))
add = Number1 + Number2
subtract = Number1 - Number2
Multiply = Number1 * Number2
Division = Number1 / Number2
Percentage = (Number1 / Number2) * 100
print(f"The result of adding {Number1} and {Number2} is: {add}")
print(f"The result of subtracting {Number2} from {Number1} is: {subtract}")
print(f"The result of multiplying {Number1} and {Number2} is: {Multiply}")
print(f"The result of dividing {Number1} by {Number2} is: {Division}")
print(f"The percentage of {Number1} relative to {Number2} is: {Percentage}")

if Number1 > 0 and Number2 > 0:
    print(f"\nThe entered numbers are positive \n")
elif Number1 < 0 and Number2 < 0:
    print(f"\nThe entered numbers are negative \n")
else:
    print(f"\nThe entered numbers have different signs \n")