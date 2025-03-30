def make_bricks(big,small,goal):
    max_big = min(goal//5,big)
    remainder = goal - (max_big*5)
    return remainder<=small

print(make_bricks(2,5,3))
print(make_bricks(2,4,13))
print(make_bricks(5,1,10))


def lone_sum(a,b,c):
    sum = 0
    if a!=b and a!=c:
        sum+=a
    if b!=a and b!=c:
        sum+=b
    if c!=a and c!=b:
        sum+=c
    return sum

print(lone_sum(3,8,11))
print(lone_sum(2,2,2))
print(lone_sum(7,8,7))

def lucky_sum(a, b, c):
    sum = 0
    if a == 13:
        return sum
    sum += a
    if b == 13:
        return sum
    sum += b
    if c == 13:
        return sum
    sum += c
    return sum


print(lucky_sum(7,8,13))
print(lucky_sum(13,1,14))


def fixteen(n):
    if 13<=n<=19 and n not in [15,16]:
        return 0
    return n

def no_teen_sum(a,b,c):
    return fixteen(a)+fixteen(b)+fixteen(c)

print(no_teen_sum(14,13,20))

def rounded(n):
    if n%10 >=5:
        return (n//10+1)*10
    else:
        return (n//10)*10
    
def round_sum(a,b,c):
    return rounded(a)+rounded(b)+rounded(c)

print(round_sum(14,18,17))
print(round_sum(5,3,4))


def close_far(a, b, c):
    return (abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2) or \
           (abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2)

print(close_far(2,3,2))

def make_chocolate(small,big,goal):
    max_big = min(goal//5,big)
    remainder = goal - (max_big*5)
    
    if remainder<=small:
        return remainder
    else:
        return -1
    

print(make_chocolate(1, 1, 9))