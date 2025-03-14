# # Question 1

# List = [];

# for i in range(0,4):
#     List.append(int(input("Enter the number: ")));


# print(List);

# # Question 2
# print(List[3]);

# # Question 3

# List_1 = ["One","Two","Three"];
# List_2 = [1,2,3];

# for i in List_2:
#     List_1.append(i);

# print(List_1)

# # Question 4

# List_5 = {1,2,3,4,5,6};

# sum = 0;
# multiplication = 1;
# for i in List_5:
#     sum = sum+i;
#     multiplication = multiplication * i;
# print(sum)
# print(multiplication)

# # Question 5

# List_6 = [10,20,30,40,50];

# sum = 0;
# total = 0;

# for i in List_6:
#     sum = sum + i;
#     total = total+1;
    
# print("Avg of all items of lists ",sum/total);

# # Question 6

# List_7=[];

# count = 0;
# for i in List_7:
#     count = count + 1;

# if(count==0):
#     print("is Empty!")
# else:
#     print("is not Empty!")

# # Question 8
# List_8 = [1,2,3,4,5];

# copyList = List_8.copy();
# print(copyList)

# # Question 9

# List_10 = [-1,2,-7,-22,11];
# NegCount = 0;
# PosCount  = 0;

# for i in List_10:
#     if(i<0):
#         NegCount+=1;
#     else:
#         PosCount+=1;
        
# print("Total Positive number is: ",PosCount)
# print("Total Neagative number is: ",NegCount)

# # Question 10

# Dict_11 = {1,2,3,4,5};
# print(len(Dict_11));


# # Question 12

# List_12 = [1,2,4,5];
# mul = 1

# for i in List_12:
#     mul*=i;

# print(mul)

# # Question 14

# List_OddEven = [1,2,3,4,5,6,7,8,9,10];

# Odd = 0;
# Even = 0;

# for i in List_OddEven:
#     if(i%2==0):
#        Even = Even + i;
#     else:
#          Odd = Odd + i;
# print("Total odd num ",Odd)
# print("Total Even num ",Even)


# Question 15 & Question 16

# a = [1,2,3,4,5];
# n = int(input("Enter the number"));

# n = n % len(a) 
# print(a[n:] + a[:n])


# Advanced sums 

# # Question 1

# List = [1,2,4,5,6,7,8,3,3];

# for i in List:
#     print(i)

# print()

# # Question 2

# List_1 = [1,2,3,4,5]
# List_1.reverse()
# print(List_1);

# print(List_1[::-1])

# for i in reversed(List_1):
#     print(i)

# # Question 3

# List_2 = [12,32,453,221];
# sum = 0;
# count = 0;

# for i in List_2:
#     sum += i;
#     count+=1;

# avg = sum / count;
 
# print("Avg of List_2 is: ",avg)
    
# for i in List_2:
#     if(i>avg):
#         print(i)


# # Question 4

# List_3 = [1,2,3,4,5,6]

# for i in range(0,len(List_3)):
#     if(i%2==0):
#         print("Even index num ",List_3[i]);
#     else:
#         print("Odd index number ",List_3[i])

# # Question 6&7&8

# List_4 = [10,11,20,21,30,31];

# OddList = [];
# EvenList = [];

# for i in List_4:
#     if(i%2==0):
#         EvenList.append(i)
#     else:
#         OddList.append(i)
        
# print("Even List is: ",EvenList);
# print("Odd List is: ",OddList)


# # Question 9 & 10 & 11

# List_9 = [-1,11,-99,45,-23,-1,-2,33,77];

# PosList= [];
# NegList=[];

# for i in List_9:
#     if(i<0):
#         NegList.append(i)
#     else:
#         PosList.append(i)

# print("Positive List is: ",PosList);
# print("Negative List is : ",NegList);

# # Question 12

# List_10 = [1,55,90,34,65];
# Biggestnum = 0;

# for i in List_10:
#     if(Biggestnum<i):
#         Biggestnum = i;

# print("Total List of Biggest number is : ",Biggestnum);

# # Question 13

# numbers = [11, 25, -1, 82, 652, 2682, 1]

# first_max = second_max = float('-inf')

# for num in numbers:  
#     if num > first_max:  
#         second_max = first_max
#         first_max = num
#     elif num > second_max and num < first_max:  
#         second_max = num  

# print(second_max)

# # Question 14

# List_15=[1,2.78,11,386,87];

# List_15.sort();
# print("Smallest number in a List is: ",List_15[0]);
# print("Highest number in a List is: ",List_15[-1]);

# Question 16

# List_Dup = [1, 2, 3, 4, 1, 3]
# i = 0

# while i < len(List_Dup):
#     j = i + 1
#     while j < len(List_Dup):
#         if List_Dup[i] == List_Dup[j]:
#             del List_Dup[j]
#         else:
#             j += 1
#     i += 1

# print(List_Dup)

# # Question 17
# List_17 = [1,2,4,4,6,8,10];

# i=0;
# while(i<len(List_17)):
#     if(List_17[i]%2==0):
#         del List_17[i];
#     else:
#         i=i+1;  
# print(List_17);

# # Question 19 & 20

# List_19 = [5, 2, 9, 1, 5, 6]

# Asc_list = sorted(List_19)
# print("Ascending:", Asc_list)


# Desc_list = sorted(List_19, reverse=True)
# print("Descending:", Desc_list)



# # Advanced sums in List

# List_1 = ["India","Australia","SouthAfrica","Newzeland"]

# print("Print List in order")
# for i in List_1:
#     print(i)
# print()

# print("Print List Reverse order")
# for i in reversed(List_1):
#     print(i)
# print()

# List_2 = [10,20,30,40,70,50]

# sum = 0;
# count = len(List_2)
# for i in List_2:
#     sum = sum + i;

# avg = sum / count
# print("Total List of avgerage is: ",avg)
# print()

# print("These numbers are greater than avgerage:")
# for i in List_2:
#     if(i>avg):
#         print(i)
# print()

# print("Even index have items: ")
# for i in range(0,count,2):
#     print(List_2[i])
# print()

# print("Odd index have items: ")
# for i in range(1,count,2):
#     print(List_2[i])
# print()


