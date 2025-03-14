# Question 1

number = 5

convertString = str(number)
print(type(convertString))


# Question 2

cel = float(input("Enter the celcius value: "))

fahren = (cel*9/5)+32

print(f"{cel} degree of celius is equal to: {fahren} degree")
print("%.2f Celsius Temperature = %.2f Fahrenheit" %(cel, fahren))

# Question 3

cm = float(input("Enter a centimeter value: "))

meter = cm/100
km = meter/ 1000
print(f"{cm} centimeter is = {meter} meter")
print(f"{cm} centimeter is = {km}kilometer") 

# Question 4

dec = int(input("Enter the Decimal Number: "))

bin = bin(dec)
oct = oct(dec)
hexa = hex(dec)

print(dec, " Decimal = ", bin, "Binary Value")
print(dec, " Decimal = ", oct, "Octal Value")
print(dec, " Decimal = ", hexa, "Hexadecimal Value")

# Question 5

km = float(input("Enter the Kilometers: "))
 
miles = km * 0.621371
 
print("%.2f Kilometers equals %.4f Miles" %(km, miles))

# Question 6

km = float(input("Please Enter the Kilometers = "))

meter = km * 1000
cm = km * 100000
mm = km * 1000000

print("%.2f Kilometers = %.2f Meters" % (km, meter))
print("%.2f Kilometers = %.2f Centimeters" % (km, cm))
print("%.2f Kilometers = %.2f Millimeters" % (km, mm))

# Question 7

words = ["Python", "Java", "Html", "Css", "Js"]
converted_str = ''

for word in words:
    converted_str += word + ' '

print(converted_str)


# Question 8

List_1 = []

number = int(input("Enter the Total List Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d List value = " % i))
    List_1.append(value)

convertTuple = tuple(List_1)

print("List Items: ", List_1)
print("Tuple Items: ", convertTuple)

# Question 9

 
miles = float(input("Enter the Miles: "))
 
kilometers = miles * 1.6093435
 
print("%.2f Miles equals %.2f Kilometers " %(miles, kilometers))\
    
    
# Question 10

tuple = ('g', 'u', 'r', 'u', 's', 'a', 'm', 'y')
print("Tuple Items =", tuple)

char = ''
for ch in tuple:
    char += ch

print("String from Tuple =", char)



