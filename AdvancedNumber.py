# Python Program to do Arithmetic Calculations using Functions

n1 = float(input("Enter a first value: "))
n2 = float(input("Enter a second value: "))
operator = input("Enter operator (+ - x %): ")
result=0;

def arithmetic_function(operator):
    match operator:
        case '+':
           result = n1+n2
        case '-' :
           result = n1-n2
        case 'x' :
           result = n1*n2
        case '/' : 
            result = n1/n2
        case _ :
            raise ValueError( "Invalid operator")
    return result

print(arithmetic_function(operator))
               
     
# Python Program to Count Number of Digits in a Number

number = int(input("Enter a number value: "))
convertString = str(number)

print("Count of number is: ",len(convertString))

# Python Program to find Factors of a Number
num = int(input("Enter a value: "))
for i in range (1,num):
    if(num%i==0):
        print(i)

Python Program to find the Factorial of a Number
factNumber = int(input('Enter a value: '))
def factorial_function(factNumber):
    if(factNumber==1):
        return 1
    return factNumber*factorial_function(factNumber-1)
print(factorial_function(factNumber))


# Python program to print the First Digit of a Number
firstNum = int(input("Enter a value: "))
isFirstDigit = 0

while(firstNum>=10):
    rem = firstNum % 10
    firstNum = firstNum // 10
    isFirstDigit = firstNum

print(firstNum)
    
# Python program to print Last Digit in a Number
LastNum = int(input("Enter a value: "))
rem = LastNum % 10

print(rem)

# Python program to find the GCD of Two Numbers

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
Gcd = 0

length = min(n1,n2)
for i in range(1,length):
    if(n1 % i == 0 and n2 % i == 0):
        Gcd = i
print("Greatest common divideder is: ",Gcd)
    
# Python program to find LCM of Two Numbers

n3 = int(input("Enter first number: "))
n4 = int(input("Enter second number: "))
Lcm = 0

length = max(n3,n4)
while(True):
    if(length % n3 == 0 and length % n4 == 0):
        Lcm = length
        break
    length+=1
print("Least common multiple: ",Lcm)

# Python program to check Palindrome Number
checkNum = int(input("Enter a value: "))
temp = checkNum
reverse = 0
while(temp>0):
    rem = temp % 10
    reverse=reverse*10+rem
    temp //=10

if(checkNum==reverse):
    print(f"{checkNum} is a palindrome number")
else:
    print(f"{checkNum} is not palindrome number")
    
# Python Program to Reverse a Number

checkReverse = int(input("Enter a value: "))
temp = checkReverse
reverse = 0
while(temp>0):
    rem = temp % 10
    reverse=reverse*10+rem
    temp //=10
print(f"{checkReverse} number after reversed this is {reverse}")

# Python program to find the Sum of Digits in a Number

check = int(input("Enter a value: "))
temp = check
sum = 0
while(temp>0):
    rem = temp % 10
    sum+=rem
    temp //=10
    
print(f"{check} number sum of digits is: {sum}")

# Python Program to Swap Two Numbers

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(f"before swapping this number: {a,b}")
a,b = b,a
print(f"after swapping this number: {a,b}")