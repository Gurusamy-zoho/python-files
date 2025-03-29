####  Pratice from python in coding bat ####


# List - 1 (Problem solving)

List = [1,2,3,4,5,6]

print(List[0]==6 or List[-1]==6)

nums = [1,2,2,1]
print(len(nums) >= 1 and nums[0] == nums[-1])


def common_end(a, b):
  if(len(a)>=1 and len(b)>=1):
       return a[0] == b[0] or a[-1] == b[-1]
  return False

print(common_end([1,2,46,78],[1,38,0,22]))


def sum_list(sumList):
    sum = 0
    if(len(sumList)>=1):
      for i in sumList:
         sum=sum+i
    return sum
print(sum_list([1,10,100,1000]))
    
# Left rotate array  

rotateLeft = int(input("Enter you want how many times rotate: "))
List_1 = [10,20,30,40,50]
rotateLeft = rotateLeft % len(List_1)
print(List_1[rotateLeft:]+List_1[:rotateLeft])

# Right rotate array

rotateRight = int(input("Enter you want how many times rotate: "))
List_2 = [10,20,30,40,50]
rotateRight = rotateRight % len(List_2)
print(List_2[-rotateRight:]+List_2[:-rotateRight])

# Reverse in Array / List

arr = [11,22,33,44,55]
reversedArr= []
for i in range(len(arr)-1,-1,-1):
   reversedArr.append(arr[i])
print(f"{arr} array of reversed array is: {reversedArr}")

# Find max_value  of array and other values change maxvalue

List_3 = [1,2,3,4,5]

max_value = List_3[0]
for i in range(1,len(List_3)):
   if(List_3[i]>max_value):
      max_value = List_3[i]

for i in range(0,len(List_3)):
    List_3[i] = max_value

 print(List_3)

# Sum of first two elements in array
rangeElements = int(input("Enter how many elements you want: "))
List_4 = []

for i in range(rangeElements):
    List_4.append(int(input(f"Enter a value of {i}: ")))

if(len(List_4)==0):
    print("Sum of first and second element is: ",0)
elif(len(List_4)<2):
    print("Sum of array is:",sum(List_4))
else:
    print("Sum of first and laast element is: ",List_4[0]+List_4[1])


rangeList_5 = int(input("Enter a first array length: "))
rangeList_6 = int(input("Enter a second array length: "))

List_5 = []
List_6 = []

for i in range(rangeList_5):
    List_5.append(int(input(f"Enter a value{i}: ")))


for i in range(rangeList_6):
    List_6.append(int(input(f"Enter a value{i}: ")))

print(f"List_5 is {List_5} and List_6 is {List_6}")
middway_5 =  len(List_5)//2
middway_6 = len(List_6)//2

print(f"[{List_5[middway_5]},{List_6[middway_6]}]")

Only show  first and last element is array

nums = [1,2,4,5,5]
print([nums[0],nums[-1]])

# True if contains 2 or 3 elements

nums = [1,2,4,5,6]

print(2 in nums or 3 in nums)

