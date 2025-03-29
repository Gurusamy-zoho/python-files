List = [1,2,3,4,5]

print(sum(num for num in List if(num%2==0)))

count = 0
for i in List:
   if(i%2==0):
      count+=1

print(f"Count of  mod divided by 2 is: {count}")

# if not given infront of 1 it's like sum of numbers
# if given it's like count of number

List_1 = [10,200,30,40,50]

minValue = List_1[0]
maxValue = List_1[0]

for i in List_1:
   if i > maxValue:
      maxValue=i
   if i<minValue:
      minValue=i

print(f"Difference between min and max value is: ",maxValue-minValue)

List_2 = [10,50,40,20,30,100]

List_2.sort()
nums = List_2[1:-1]
print(sum(nums)//len(nums))


List_3 =  [7,13,5,8,90,13]

sum = 0

for i in List_3:
   if(i == 13):
      continue
   else:
      sum+=i

print(f"Sum of array without 13 is: ",sum)

def sum13(nums):
    total = 0
    jump = False
    for i in range(len(nums)):
        if jump:
            jump = False
            continue
        if nums[i] == 13:
            jump = True
            continue
        total += nums[i]
    return total

sum13([13,1,4,13,5,13])


def sum67(nums):
    total = 0
    skip = False
    for num in nums:
        if skip:
            if num == 7:
                skip = False
            continue
        if num == 6:
            skip = True
            continue
        total += num
    return total

sum67([1, 2, 2, 6, 99, 99, 7])

def has22(nums):
    for i in range(len(nums) - 1): 
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

has22([1,2,2,1])
