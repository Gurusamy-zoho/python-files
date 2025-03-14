# a = int(input("Enter a number: "));
# b = int(input("Enter a another number: "));

# for i in range(a+1,b):
#     print(i)
 
# print()

# e_count = 0
# o_count = 0;
# for j in range(a,b):
#     if(j%2==0):
#         print(j)
#         e_count+=1
#     else:
#         o_count+=1
        
# print("Count of even number is: ",e_count)
# print("Count of odd number is :",o_count)

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter secoond number: "))

# for i in range(n1,n2):
#     if(i%3==0 and i%5==0):
#         print(i)
        

# for evenNum in range(10,20,2):
#     print(evenNum)
    
# for oddNum in range(1,10,2):
#     print(oddNum)
   
# sum = 0; 
# for i in range(1,11):
#     a = int(input("Enter number "+str(i)+": "))
#     sum+=a
# print("Total sum : ",sum)

# list_cube = [];


# for i in range(1,6):
#     num = int(input())
#     cube = num*num*num
#     print("Number is: ",num," and cube of ",num," is: ",cube)
  
# star patterns for nested loops

for i in range(1,6):
    for j in range(1,i):
        print("* ",end="")
        print()