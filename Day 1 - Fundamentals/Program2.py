user_name ="Bro_Code"
year = 2026
pi = 3.14
is_admin = True

#print(f"Hello {user_name}\nWelcome to the year {year}\nThe value of pi is {pi}\nIs admin working today? : {is_admin}")


input1 = int (input("Enter first number: "))
input2 = int (input("Enter second number: "))
result = input1 + input2
print(f"The result of adding {input1} and {input2} is: {result}")
if input1>input2 and input2>0:
    Difference = input1 - input2
    print(f"The difference of {input1} and {input2} is:{Difference}")
else:
    print("The difference cannot be calculated as the second number is greater than the first number or the second number is less than or equal to zero")   
    Div = float(input1) / float(input2)
    print(f"The division of {input1} and {input2} is:{Div}")