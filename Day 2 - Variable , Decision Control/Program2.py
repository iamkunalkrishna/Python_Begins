# Program to check whether the entered number is positive, negative or 0.

P=int(input("Enter the number: "))
if P>0:
    print("You have entered a postitive number")
elif P==0:
    print("You have enetred 0")
else:
    print("You have entered a negative number")

# Program to to use the decision making statement

Firstsub = int(input("Enter your marks in 1st subject: "))
Secondsub = int(input("Enter your marks in 2nd subject: "))
Thirdsub = int(input("Enter your marks in 3rd subject: "))
Fourthsub = int(input("Enter your marks in 4th subject: "))
Total=Firstsub+Secondsub+Thirdsub+Fourthsub
Agg=int(Total/5)
if Agg>75:
    print(f"Congratulations !! You are passed with distinction and received {Agg}% aggregate")
elif Agg<75 and Agg>=60:
    print(f"Congratulations !! You are passed with First Dision and received {Agg}% aggregate")
elif Agg<60 and Agg>=50:
    print(f"Congratulations !! You are passed with Second Dision and received {Agg}% aggregate")
elif Agg<50 and Agg>=40:
    print(f"Congratulations !! You are passed with Third Dision and received {Agg}% aggregate")
else:
    print(f"Sorry !! You are failed as you have received {Agg}% aggregate")

    
# Program to check whether the entered two number are equal or not

P=int(input("Enter the first number: "))
Q=int(input("Enter the second number: "))
if P==Q:
    print("The entered numbers are equal !!!",end=" ")
else:
    print("The entered numbers are not equal !!!", end=" ")
