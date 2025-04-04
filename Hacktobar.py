# Question no : 2

caves = [["gold","silver","emerald"],["emerald","diamond","ruby"],["sapphire","silver","platinum"]]
known_elements = set(["gold","silver","platinum"])

def unKnownElements(caves,known_elements):
    unknown_elements =[]
    for i in range(len(caves)):
        for j in range(len(caves[0])):
            if(caves[i][j] not in known_elements):
                   unknown_elements.append(caves[i][j])
                   known_elements.add(caves[i][j])
    return unknown_elements

print(unKnownElements(caves,known_elements))
                   
# Question no: 5

scene = [[1,2,3],[4,5,6],[7,8,9]]
factor = 3

def magnifired_scene(scene,factor):
     for i in range(len(scene)):
          for j in range(len(scene[0])):
              scene[i][j] = scene[i][j]*factor
     return scene

print(magnifired_scene(scene,factor))

# Question no : 6

trail = [1,3,2,5,4,7]

def complete_trek(trail):
     energy = 0
     for i in range(len(trail)-1):
        if trail[i+1]>trail[i]:
             energy += trail[i+1] - trail[i]
     return energy

print("Need energy to enough completed to trek is: ",complete_trek(trail))

# Question no 15

titles = ["Introduction","Conculsion","Appendix","History","Methods","Apple","Appolo"]

def  alphabet_wise(titles):
     order_wise_title = []
     for i in range(len(titles)):
          for j in range(len(titles)-i-1):
               if(titles[j]>titles[j+1]):
                    titles[j],titles[j+1] = titles[j+1],titles[j]
     return titles

print(alphabet_wise(titles))

# Question no 4


X = 1000
countries = {"Japan":1000,"Brail":300,"Australia":500}

def sorted_countries_values(countries,X):
     convert_list = list(countries.items())

     for i in range(len(convert_list)):
          for j in range(len(convert_list)-i-1):
              if convert_list[j][1]>convert_list[j+1][1]:
                   convert_list[j],convert_list[j+1] = convert_list[j+1],convert_list[j]
     
     going_country = []
     for i in range(len(convert_list)):
          if convert_list[i][1] < X :
               going_country.append( convert_list[i][0])
               X-=convert_list[i][1]
     return going_country

print(sorted_countries_values(countries,X))          
                   

# Question no : 17

n = 3
key_word = ["Hello","Journal","Secret"]

def shift_keyword(key_word,n):
     new_list = []
     empty = ""
     for word in key_word:
          for letter in word:
              empty+= chr(ord(letter)+n)
          new_list.append(empty)
          empty = ""
     
     return new_list

print(shift_keyword(key_word,n))

