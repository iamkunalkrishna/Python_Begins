# Program to understand the loop concept

x = 2
while(x<=10):
    if (x%2 == 0):
        print(x)
    else:
        print("The number is Odd")
    x+=1

# Program to calculate the sum and average of first 10 numbers.

i=0
sum=0
while(i<11):
    sum= sum+i
    i+=1
avg=sum/10
print(f"The sum of first 10 numbers is {sum} and average is {avg}")
