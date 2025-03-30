def string_items(s,n):
    return s*n

print(string_items("Hello",3))
print(string_items("John",2))


def string_bits(s):
    return s[::2]

print(string_bits("Hello"))
print(string_bits("Dowell"))

def string_splosion(s):
     result = ""
     for i in range(len(s)):
         result+=s[:i+1]
     return  result

print(string_splosion("Zoho"))
print(string_splosion("Zohoschools"))


def last2(s):
    if len(s)<2:
        return 0
    last_two = s[-2:]
    count = 0
    for i in range(len(s)-2):
        if(s[i:i+2]==last_two):
            count+=1
    return count

print(last2("hiddxxhixxhihi"))

def count9(arr):
    return arr.count(9)

print(count9([78,0,9,99,11,9,63,55,9,3]))


