# # Question 1
# str = "JohnDoe";

# char = str[0];
# print(f"ASCII Value is = {ord(char)}");

# # Question 2

# name = "JohnDoe";

# for i in range (0,len(name)):
#     char = name[i];
#     print(f"{name[i]} ASCII Value is = {ord(char)}");
    
# # Question 3

# word_1 = input("Enter a string value: ");
# word_2 = input("Enter another string value: ");

# print("word_1 , word_2 Concetation is: "+word_1+word_2);
# print("word_1 , word_2 , with white space string value: "+word_1+" "+word_2);

# # Question 4

# str = "helloworld";
# print(str.upper())

# Dup_str = "";

# for i in range(0,len(str)):
#     char = ord(str[i]) - 32;
#     ch = chr(char)
#     Dup_str = Dup_str + ch;
    
# print(Dup_str);

# # Question 5

# string_1 = "HELLOWORLD";
# print(string_1.casefold())

# Dup_String = "";

# for i in range(0,len(string_1)):
#     char = ord(string_1[i]) + 32
#     ch = chr(char)
#     Dup_String += ch

# print(Dup_String)

# # Question 6

# word = "Hello Wolrd"

# Dup_word =""
# for i in word:
#     Dup_word += i

# print(Dup_word)

# # Question 7

# String_value = "malayalam"
# Reverse_String = ""

# for i in range(len(String_value)-1,-1,-1):
#     Reverse_String += String_value[i]
    
# if(String_value==Reverse_String):
#     print(f"{String_value} word is palindrome")
# else:
#     print(f"{String_value} word is not palindrome")

# # Question 8


# String_1 = input("Enter a string value: ")
# String_2 = input("Enter another string: ")

# s1 = sorted(String_1)
# s2 = sorted(String_2)

# if (s1==s2):
#     print("This words are anagram")
# else:
#     print("This words are not anagram")

# # Question 9

# str = input("Enter a string value: ")
# char = input("Enter a character value: ")

# isChar = False
# i = 0
# while(i<len(str)):
#     if(char==str[i]):
#         isChar = True
#         break
#     i+=1
# if(isChar==True):
#     print(f"The first occurence of characters is :{i}")
# else:
#     print("The first occurence character is not avaliable") 

# # Question 10

# str = input("Enter a string value: ")
# char = input("Enter a character value: ")


# isChar = False
# i = len(str)-1
# while(i>=0):
#     if(char==str[i]):
#         isChar = True
#         break
#     i-=1
# if(isChar==True):
#     print(f"The last occurence of characters is :{i}")
# else:
#     print("The last occurence character is not avaliable") 

# # Question 11

# Val_str = "Helloworld"

# for i in Val_str:
#     print(i)

# # Question 12

# str = "GurusamySivasankar"

# countOfCharacters = 0

# for i in str:
#     countOfCharacters+=1

# print(countOfCharacters)

 # # Question 13

# str = input("Enter a string value: ")
# char = input("Enter a char value: ")

# for i in range(0,len(str)):
#     if(char==str[i]):
#         print(f"Index of charachters is: {i}")

