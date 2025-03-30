def party(cigars,weekend):
    if  weekend:
        return cigars>=40
    return cigars>=40 and cigars<=60

print(party(30,False))
print(party(50,False))
print(party(70,True))

def fashion(you,date):
    if you<=2 or  date<=2:
        return 0
    elif you>=8 or date>=8:
        return 2
    else:
        return 1

print(fashion(8,7))
print(fashion(3,2))
print(fashion(5,2))

def squirrel_play(temp, is_summer):
    if is_summer:
      return 60 <= temp <= 100
    else:
        return 60 <= temp <= 90

print(squirrel_play(75,True))
print(squirrel_play(95,False))
print(squirrel_play(90,True))

def caught_speeding(speed,birthday):
    if birthday:
        speed -=5
    if speed<=60:
        return 0
    elif speed <=80:
        return 1
    else:
        return 2
    
print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))

def sortasum(a,b):
    sum = a+b
    if 10<=sum<=19:
        return 20
    return sum

print(sortasum(10,3))
print(sortasum(7,11))
print(sortasum(10,19))

def alarm_clock(day,vactaion):
    if vactaion:
        if day ==  0 or day == 6:
            return 'off'
        else:
            return '10:00'
    else:
        if(day==0 or day==6):
            return '10:00'
        else:
            return '7:00'
        

def lover6(a,b):
    return a==6 or b==6  or abs(a-b)==6 or  a+b == 6

print(lover6(4,2))
print(lover6(6,10))
print(lover6(2,2))

def in1to10(n,outside_mode):
    if outside_mode:
        return n>=10 or n<=1
    else:
        return 1<=n<=10
    
print(in1to10(11, True))

def near_ten(num):
       return num % 10 <= 2 or num % 10 >= 8

print(near_ten(70))
print(near_ten(78))