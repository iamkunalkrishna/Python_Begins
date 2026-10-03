# Program to swap two numbers using a temporary variable

Number1 = input("Enter the first number: ")
Number2 = input("Enter the second number: ")
Num = Number1
Number1= Number2
Number2 = Num
print(f"\nThe number after swapping is: \n First Number is:{Number1} \n Second Number is:{Number2}")

# Program to read the address of a user and print it in a proper format

Address = input("Enter your address: ")
print(f"Your address is: {Address[:3]}")
print(f"Your address is: {Address[4:7]}")
print(f"Your address is: {Address[8:12]}")
print(f"Your address is: {Address[9:12]}")