# Program to swap two numbers using a temporary variable

Number1 = input("Enter the first number: ")
Number2 = input("Enter the second number: ")
Num = Number1
Number1= Number2
Number2 = Num
print(f"\nThe number after swapping is: \n First Number is:{Number1} \n Second Number is:{Number2}")
