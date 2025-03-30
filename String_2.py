def repeat_two(s):
    result = ""
    for i in s:
        result+=i*2
    return  result

print(repeat_two("The"))
print(repeat_two("Hii there!"))

def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if((str[i]+str[i+1])=='hi'):
          count+=1

    return count

print(count_hi("hihllohihi"))
print(count_hi("hihi"))

def same_number(word):
    dog_count = 0
    cat_count = 0

    for i in range(len(word)-2):
        if((word[i]+word[i+1]+word[i+2])=="cat"):
            cat_count+=1
        if((word[i]+word[i+1]+word[i+2])=="dog"):
            dog_count+=1
        
    if dog_count == cat_count:
        return True
    else:
        return False


print(same_number("catdofcatdogcagdog"))
print(same_number("catdoug"))

def count_code(str):
    count = 0
    for  i in range(len(str)-3):
        if str[i:i+2]=='co' and str[i+3]=='e':
            count+=1
    return count

print(count_code("cozeiicodeiicooe"))

def lastin_same(f,s):
    f = f.lower()
    s = s.lower()
    slen = len(s)

    return f[-len(s):] == s or s[-len(f):] == f

print(lastin_same("theAbc","abc"))
print(lastin_same("abc","AbCXa"))