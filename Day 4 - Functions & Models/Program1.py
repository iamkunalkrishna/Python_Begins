# Program of def
m=int(input("Enter a number: "))

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
    print(f"Sorry !! You are failed as you have received {Agg}% aggregate"
