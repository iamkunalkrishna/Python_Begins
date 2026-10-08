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

# Program to print 20 horizontal asterisks(*)

i=1
while(i<21):
    print("*",end="")
    i+=1

# Program to practise loop
i=1
while(i<20):
    print(f"The loop ran {i} number of times")
    i+=5

# Program to sum a numbers between m to n

m=int(input("Enter the range, (x cordinate)"))
n=int(input("Enter the range, (y cordinate)"))
sum=0
while(m<=n):
    sum+=m
    m+=1
print(f"The shortest between those distace is: {sum} ")


# Program to count the numbers until -1 is reached and also tell the number of +ve, -ve and 0.

post=0
neg=0
zero=0
while(1):
    m=int(input("Enter the number: "))
    if (m==-1):
        break
    if (m==0):
        zero+=1
    elif (m>0):
        post+=1
    else:
        neg+=1

print(f"Count of Postive: {post}")
print(f"Count of negative: {neg}")
print(f"Count of Zeroes: {zero}")
  

