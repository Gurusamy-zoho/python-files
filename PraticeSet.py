# Python Program to create a Set
setVal = {10,20,30,40,50}
print(setVal)

# Python program to Count Even and Odd Numbers in Set
my_set = {7, 93, 86, 45, 33, 67, 13, 27, 77, 100}
EvenSet = set()
OddSet = set()

for i in my_set:
    if i % 2 == 0:
        EvenSet.add(i)
    else:
        OddSet.add(i)

print("Even Numbers Set:", EvenSet)
print("Odd Numbers Set:", OddSet)


# Python program to Count Positive and Negative Numbers in Set
setVal = {-20,11,-99,-53,89,25,58}
setPositive = set()
setNegative = set()

for i in setVal:
    if i>0:
        setPositive.add(i)
    else:
        setNegative.add(i)

print("Positive number set",setPositive)
print("Negative number set",setNegative)

# Python program to Iterate Set Items

my_set = {7, 93, 86, 45, 33, 67, 13, 27, 77, 100}
for item in sorted(my_set):
    print(item)

#Python program to Print Largest Set Item

my_set = {7, 93, 86, 45, 33, 67, 13, 27, 77, 100}

largest_item = max(my_set)
print("Largest Item in the Set:", largest_item)

# Python program to find Length of a set

my_set = {7, 93, 86, 45, 33, 67, 13, 27, 77, 100}
length = len(my_set)
print("Length in the Set:", length)

my_set = {7, 93, 86, 45, 33, 67, 13, 27, 77, 100, -7, -86, -13, -100}

# Even Numbers in Set
even_numbers = {x for x in my_set if x % 2 == 0}
print("Even Numbers in Set:", even_numbers)

# Odd Numbers in Set
odd_numbers = {x for x in my_set if x % 2 != 0}
print("Odd Numbers in Set:", odd_numbers)

# Positive Numbers in Set
positive_numbers = {x for x in my_set if x > 0}
print("Positive Numbers in Set:", positive_numbers)

# Negative Numbers in Set
negative_numbers = {x for x in my_set if x < 0}
print("Negative Numbers in Set:", negative_numbers)

# Sum of Even and Odd Numbers in Set
sum_even = sum(x for x in my_set if x % 2 == 0)
sum_odd = sum(x for x in my_set if x % 2 != 0)

print("Sum of Even Numbers:", sum_even)
print("Sum of Odd Numbers:", sum_odd)

# Smallest and Largest Item in Set
smallest_item = min(my_set)
largest_item = max(my_set)

print("Smallest Item in the Set:", smallest_item)
print("Largest Item in the Set:", largest_item)

