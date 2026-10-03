from unittest import result


user_name ="Bro_Code"
year = 2026
pi = 3.14
is_admin = True

#print(f"Hello {user_name}\nWelcome to the year {year}\nThe value of pi is {pi}\nIs admin working today? : {is_admin}")


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