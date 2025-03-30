def sleep_in(weekday, vacation):
      return not weekday or vacation

print(sleep_in(False,False))


def smile_in(a_smile,b_smile):
      return a_smile==b_smile

print(smile_in(True,False))

def sum_double(a,b):
      if a==b:
         return 2*(a+b)
      else:
           return (a+b)
      
print(sum_double(2,6))
print(sum_double(4,4))

def diff21(n):
     if n>21:
          return 2* abs(n-21)
     else:
          return abs(21-n)
     
print(diff21(51))
print(diff21(7))

def parrot_trouble(talking,hour):
     if talking and (hour>20 or hour<7):
          return True
     return False

print(parrot_trouble(True,9))
print(parrot_trouble(True,2))

def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10
print(makes10(5,3))
print(makes10(10,5))

def near_hundred(n):
     return abs(n-100)<=10 or abs(n-200)<=10

print(near_hundred(190))
print(near_hundred(-100))

def pos_neg(a,b,negative):
     if negative:
          return a<0 and b<0
     else:
          return  (a<0 and b>0) or (a>0 and b<0)
     
print(pos_neg(-1,1,False))
print(pos_neg(-1,-1,True))

def not_string(s):
     if s.startswith("not"):
          return s
     else:
          return "not "+s
     

print(not_string("going"))

def missing_char(s,n):
     return s[:n]+s[n+1:]

print(missing_char("Hello",2))
print(missing_char("World",3))

def front_back(s):
     if len(s)<=1:
          return s
     return s[-1]+s[1:-1]+s[0]

print(front_back("Devilliers"))
print(front_back("Virat"))

def first_char(s):
     front =s[:3]
     return front*3

print(first_char("Hello"))
print(first_char("World"))
print(first_char("Good"))