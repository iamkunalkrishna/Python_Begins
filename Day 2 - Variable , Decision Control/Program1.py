# Program to check the voting eligibility and the difference if there is any in between

age = int(input("Enter your age: "))
if age>=18:
    print("Congratulations! You are eligible to vote ")
else:
    need = 18 - age
    print(f"There is still {need} years needed to be a voter")

# Program to check the larger of two number

N1 = int(input("Enter first Number F: "))
N2 = int(input("Enter second Number S: "))
if N1>N2:
    print(f"The first number F: {N1} is greater than the second number S: {N2}")
else:
    print(f"The second number S: {N2} is greater than the first number F: {N1}")

# Program to distribute bonus as per the salary and gender

Salary = float(input("Enter the salary: "))
gen = str(input("Enter your gender: "))
bonf = Salary*0.1 
Over = bonf + Salary
bonm = Salary*0.05
Man = bonm + Salary

if gen == "F" or gen == "f":
    print(f"Your bonus is Rs {bonf} and the overall salary is Rs {Over} ")
else:
    print(f"Your bonus is Rs {bonm} and the overall salary is Rs {Man} " )


# Program to tell the inteval of the number entered by user

num = int(input("Enter the number between 1 to 50: "))
if num >0 and num <=10:
    print("Entered number is within th range 1 to 10")
if num >10 and num <=20:
    print("Entered number is within th range 11 to 20")
if num >20 and num <=30:
    print("Entered number is within th range 21 to 30")
if num >30 and num <=40:
    print("Entered number is within th range 31 to 40")
if num >40 and num <= 50:
    print("Entered number is within th range 41 to 50")
    