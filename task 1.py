#arithmetic operators
#addition
a=10
b=5
print("add:",a+b)
#difference
a=10
b=5
print("sub:",a-b)
#product
a=10
b=5
print("multiply:",a*b)
#divide
a=10
b=5
print("divide:",a/b)
#floor division
a=10
b=5
print("floor division:",a//b)
#remainder
a=10
b=5
print("modulus:",a%b)
#square of a number
a=10
print("expo:",a**b)
#total average of 5 subject marks
a=85
b=90
c=95
d=96
e=87
#total
print("add:",a+b+c+d+e)
#average
print("divide:",a+b+c+d+e/5)

#last 2 digit of a number
a=int(input("enter a:"))
b=a%100
print("last digit",b)
#last 3 digit of a number
a=int(input("enter a:"))
b=a//1000
#assignment operators
#assign name to variable
name="badriga"
print(name)
#assign 100 to a variable and add 50 using '+='
a=100
a+=50
print(a)
#subtract 20 from a balance using '-='
a-=20
print(a)
#multiply number by 5 using '*='
a=5
a*=5
print(a)
#divide a number by 2 using'/='
a=8
a/=2
print(a)
#find the remainder using'%='
print(a)
#calculate the square of number using'**='
a=100
a**=100
print(a)
#comparison operators
#get two numbers and check whether they are equal
a=10
b=5
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a==b)
#two numbers are not equal
a=10
b=5
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a!=b)
#biggest of two numbers
a=10
b=100
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a>b)
print(a<b)
#student is eligible for voting(age 18 or above)
a>=18
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a>=b)
#student passed(mark 35 or above)
a>=35
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a>=b)
#number is between 1 and 100
a=>1
b=<100
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a<b)
#logical operators
#check whether a number is positive and even
a=10
print(a>0 and a/2)
#person eligible for voting(age 18 or above) and has an Id
a=25
print(a>=18)
#check whether a student passed in atleast one of two subjects
a=65
b=85
print(a>40 or b>40)
#check whether a number is between 10 and 50
a=76
print(a>10 and a<50)
#check whether number is not equal to zero
a=7
print(not(a==2))
#membership operators
#letter a is present in a name
x=["badriga"]
print("a" in x)
#python present in list of programming language
a=["python, java"]
print=("python" in a)
#particular number exist in a list
a=["1,2,3,4,5"]
print("2" in a)
#character is not present in a string
a=["@,$,%,^,&"]
print("*" in a)
#identity operators
#create two variables with the same value and compare them using 'is'
a=[1,2,3,4]
b=[1,2,3,4]
a=b
print(a is b)
print(a is not b)

#Bitwise Operators
a=10
b=5
print("%",a&b)
print("#",a|b)
print("@",a^b)
print("!",~b)

#Real-Time Mini Tasks
#Get name and 5 subject marks. Calculate total, average and pass/fail
name=input("name of the student")
s1=int(input("Mark1:"))
s2=int(input("Mark2:"))
s3=int(input("Mark3:"))
s4=int(input("Mark4:"))
s5=int(input("Mark5:"))
avg=s1+s2+s3+s4+s5/5
for i in avg():
    if i>250:
        print("Pass",i)
    else:
        print("Fail",i)

#Get units consumed and calculate the bill using a given per unit rate
a=int(input("units consumed"))
b=10
print("Total electricity bill=",a*b)

#Get product price and quantity. Calculate total amount and discount.
price=int(input("price"))
quantity=int(input("quantity of the product"))
print("Total Price:",quantity*price)
print("Total Discount:",quantity*price/20*100)

#Get age and check eligibility
age=int(input("Age"))
a=age        
print("Eligible to Vote",a>18)
print("Not Eligible to Vote",a<18)
#Check whether a number is even or odd using `%`.
a=int(input("enter number"))
b=a%2==0
c=a%2!=0
print("number is even",b)
print("number is Odd",c)

#Get three numbers and find the largest
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
greater=max(a,b,c)
print("The Largest Number is",greater)








