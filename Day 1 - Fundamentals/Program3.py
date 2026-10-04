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

# Program to calculate the simple interest and compound interest

Principal = float(input("Enter the principal amount: "))
Rate = float(input("Enter the rate of interest: "))
Time = float(input('Enter the tenure of loan: '))
SI = (Principal*Rate*Time)/100
print(f"The Simple Interest on Rs int({Principal}) at the rate of int({Rate})% until int({Time}) year is float({SI})")

# Program for the if else statements

age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote !!")
else:
    print("You are a minor $%^")


# Program to check if the character entered by user is number, alphabet or special character

p = input("Enter any key: ")
if (p.isalpha()):
    print ("The enetered key is a alphabet !!")
if (p.isdigit()):
    print("The entered key is a digit !!")
if (p.isspace()):
    print("The eneteres key is a speical character !!!")