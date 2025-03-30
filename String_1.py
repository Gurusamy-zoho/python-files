def hello_name(name):
    return f"Hello {name}!"

print(hello_name("Bob"))
print(hello_name("Alice"))
print(hello_name("X"))

def makeabba(str1,str2):
    return str1+str2+str2+str1

print(makeabba("Hiii","Bye"))
print(makeabba("Hello","Nice"))

def make_tags(tag,word):
    return f"<{tag}>{word}</{tag}>"

print(make_tags("h1","Zohoschools"))

def make_out_word(outside,word):
   return outside[:2]+word+outside[2:]

print(make_out_word("<<>>","Yahoo"))
print(make_out_word("####","Pratice python"))

def last_two(str):
    return str[-2:]*3

print(last_two("Hello"))
print(last_two("Nice"))

def first_two(str):
    return str[:2]

print(first_two("Good"))
print(first_two("Bad"))
