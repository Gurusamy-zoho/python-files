List = ["John","Doe","Alias","Rock"];

my_Dict = {};

for i in range(0,len(List)):
    my_Dict[i]=List[i];
    
print(my_Dict)

for i in range(0,len(my_Dict)):
    print("Keys:",i," Values:",my_Dict[i]);
    
    
# Tutorial Gateway

# 1) Pyhton Program to Add key value pair to dictionary
 
Dict = {};

Dict["name"] = "Guru";
Dict["Age"] = 18;

print(Dict)

# 2) Python Program to check if a key exits in a Dictionary

Dict_val = {0:"Guru",1:"Siva"};

keys = int(input("Enter a key: "));

for i in Dict_val:
    if(i==keys):
        print("True")
        break;
    else:
        print("Else")
# 3) Python program to coujt words in a string use in Dictinary

my_dict = {1:"All the students are informed that",2:"Our School pricipal has orgainsed"};

countWords = 0;
for i in my_dict:
    Words = my_dict[i];
    for j in range(1,len(Words)):
        if(Words[j]==" "):
            countWords+=1
        else:
            continue
    print("Total words in key",countWords+1)
    countWords=0;
    
Dict = {};

for i in range(1,10):
    Dict[i] = i*i;
print(Dict)

MappingDict={}
List_1 = ["Guru","Siva"];
List_2 = [17,18];

for i in range(0,len(List_2)):
    MappingDict[List_1[i]] = List_2[i];

print("MappingDictionary ",MappingDict);

Dict_1 = {0:"John",1:"Doe"};
Dict_2 = {2:"Alias",3:"Khan"};

for i in Dict_2:
    Dict_1[i] = Dict_2.get(i)

print(Dict_1)

Dict_3 = {0:"Jospesh",1:"Vijay"};
keys = int(input("Enter a key only: "));

del Dict_3[keys];
print(Dict_3)

Dict_4 = {0:19,1:11,2:30,3:40};

sum = 0;
for i in Dict_4:
    sum = Dict_4[i]
    sum += sum

print(sum)

