Logic's of python

# Sum of values :

a = 10;
b = 15;
c = 5;

print("sum of a+b+c",a+b+c);

# Find positive number or negative number

num = int(input("Enter a value: "));

if(num>0):
    print("Positive number")
else:
    print("Negative number")
    
# Check even or odd number

num = int(input("Enter a value: "));

if(num%2==0):
    print("Even number")
else:
    print("Odd number")

# Check charachters vowles or not vowels

charValue = input("Enter a characthers: ");

if(charValue=='a' or charValue=='e' or charValue=='i' or charValue == 'o' or charValue == 'u' or charValue=='A' or charValue == 'E' or charValue == 'O' or charValue == 'I' or charValue=='U'):
    print("This is vowels charachters")
else:
    print("This is not a vowels or constant")


# Check is letter alphabet or not 

letter = input("Enter a charachter: ")

if(letter>='a' and letter<='z' or letter>='A' and letter<='Z'):
    print("This is alphabetic charachters")
else:
    print("This is not alphabetic charachters")

# Finding Average of N numbers 

rangeValue = int(input("How many values you want: "))
count = 0
sum = 0
for i in range(0,rangeValue):
    value = int(input("Enter a values: "))
    sum = sum+ value
    count+=1

avg = sum / count
print("Avg of N numbers is:",avg)


# Print all number numbers divisable by given numbers

rangeValue = int(input("Enter range value: "))
divisableValue = float(input("Enter divisible value: "))

if divisableValue == 0.0:
    raise ValueError("Any number can't be divided by zero")

divisableValue = int(divisableValue)

for i in range(1, rangeValue + 1):
    if i % divisableValue == 0:
        print(i)

Find a greade for students

dict={
    "Renuga" : 581,
    "Karthika" : 539,
    "Jeyashree" : 514,
    "Karthick" : 541,
    "Kishon karthik" : 536,
    "Gurusamy" : 504,
    "Arun vasantha raja" : 525,
    "Parameshwaran" : 514,
    "Sujith" : 501,
    "Mohanraja" : 444  
};

for name,marks in dict.items():
    avg = (marks / 600) * 100
    
    if(avg>=95):
        print(name," is A++ grade student")
    elif(avg>=85 and avg<95):
         print(name," is A+ grade student")
    elif(avg>=80 and avg<85):
        print(name," is a A grade student")
    else:
        print(name," is B grade student")

# Swapping to numbers 

num1 = int(input("Enter first value: "))
num2 = int(input("Enter another value: "))

print("before swapping: ",num1,num2)

num1,num2 = num2,num1
print("after swapping: ",num1,num2)

# Floor divisions

num1 = int(input("Enter a value: "))
num2 = int(input("Enter divided value: "))

print(num1," divided by ",num2," queoitent is:",num1/num2)
print(num1," divided by ",num2," remainder is:",num1%num2)
print(num1," divided by ",num2," floor division is:",num1//num2)

# Range of add or even numbers

rangeVal = int(input("Enter a value: "))

for i in range(1,rangeVal):
    if(i%2==0):
        print(i," is even number")
    else:
        print(i," is odd number")

# Multiplication table 

rangeMultiplication = int(input("Enter range value: "))
multiplicationTable = int(input("Enter you want table value: "))

for i in range(1,rangeMultiplication+1):
    print(i," X ",multiplicationTable," = ",i*multiplicationTable)

#Miles to convert Kilometer

km = float(input("Enter a km value: "))
miles = km * 0.62137

print(km," kilometers is equal to ",round(miles,2)," miles")
print(f"{km} kilometers is equal to {miles:.2f} miles")

miles = float(input("Enter miles value: "))
km = miles/0.62137;

print(f"{miles} miles is equal to {km:.2f} kilometer")

# Celicus to Faherinhet

celcius = float(input("Enter celcius: "))
faherinhet = float(input("Enter faherinhet: "))

f = (1.8*celcius)+32
print(f"{celcius} celcius is equal to {f} faherinhet")

c = (faherinhet-32)/1.8
print(f"{faherinhet} faherinhet is equal to {c} celcius")


# Find area of triangle 

a = float(input("Enter a value: "));
b = float(input("Enter b value: "));
c = float(input("Enter c value: "));

s = (a+b+c)/2
print("semi-perimeter is: ",s)

area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"area of triangle sides of {a,b,c} is: {area:.2f}")

# Find largest number is among three

List=[]

rangeVal = 3
for i in range(0,rangeVal):
    List.append(int(input("Enter a value: ")))

print("Largest value is: ",max(List))

# Sum of natural numbers 

n = int(input("Enter n value: "))

naturalNumber = (n*(n-1))/2
print(f"Sum of {n} natural number is: {naturalNumber}")

number = int(input("Enter a value: "))

if(number<0):
    print("Please enter a positive number")
else:
    sum = 0
    i=0
    while(i<=number):
        sum+=i
        i+=1
    print(f"Sum of {number}natural number is: {sum}")

# Factorial Numbers 

num = int(input("Enter a number: "))
fact = 1;
for i in range(num,1,-1):
    if(i==1):
        fact=fact*1
        break;
    else:
        fact = fact*i

print(f"{num} factorial is: {fact}")

def factorial(num):
    if(num==0 or num==1):
        return 1
    
    return num*factorial(num-1)

print(factorial(5))


# Fibbonacci series 

n = int(input("Enter how many series you want: "))

first = 1
second = 1

List = [1, 1]

while len(List) < n:
    f = first + second
    s = f + second
    List.append(f)
    if len(List) < n:
        List.append(s)
    
    first = f
    second = s

print(List)

# Find out is Leapyear or not Leapyear

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It's a leap year and a century year")
elif year % 100 == 0:
    print("It's not a leap year (century year)")
elif year % 4 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")

    
# Find Armstrong number

number = int(input("Enter a value: "))


sum = 0
count = len(str(number))
temp = number

while(temp>0):
    rem = temp % 10
    sum = sum + rem**count
    temp = temp // 10
    
    
if(number==sum):
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not a armstrong number")


# Range with two between print armstrong number

start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

for i in range(start,end+1):
    sum = 0
    count = len(str(i))
    temp = i

    while(temp>0):
      rem = temp % 10
      sum = sum + rem**count
      temp = temp // 10
    
    
    if(i==sum):
       print(f"{i} is a armstrong number")
   
    
import calendar

print(calendar.month(2025,3))
print(calendar.calendar(2050))
print(calendar.weekday(2025,3,13))
print(calendar.isleap(2000))
print(calendar.calendar(2026,2,2,3,4))

