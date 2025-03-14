jsonObj = {
    "name": "Rahul Sharma",
    "email": "rahulsharma123@gmail.com",
    "age": 25,
    "gender": "Male",
    "location": "dhwi",
    
        
     "personal_status":{}
}


name = jsonObj.get("name");
user_name = name.replace(" ","")

if("name" in jsonObj ):
    if(not user_name=="" and isinstance(user_name,str) and user_name.isalpha()):
        print("Username successfully add")
    else:
        print("Enter correct username")
else:
    print("name key is not found.")
    
user_email = jsonObj.get("email");

if("email" in jsonObj):
    if(not user_email=="" and isinstance(user_email,str)):
        print("Useremail added successfully")
    else:
        print("Enter correct email")
else:
    print("email key is not found")
    
user_age = jsonObj.get("age")

if("age" in jsonObj):
        if(not user_age==0 and isinstance(user_age,int) and (user_age>=18 and user_age<120)):
            print("Userage added successfully")
        else:
            print("Enter correct age between 18 to 120")
else:
    print("age key is not found")
    
user_gender = jsonObj.get("gender")

if("gender" in jsonObj):
        if(not user_gender=="" and isinstance(user_gender,str) and user_gender in ["Male","Female","Other"]):
            print("Usergender added successfully")
        else:
            print("Enter genter in ['Male','Female','Other']")
else:
    print("genter key is not found")
    
user_location = jsonObj.get("location")



isCountry = False;
isCity = False;

Country = ["India","Australia","Southkoera","Japan","China"]
City = ["Mumbai","Kolkata","Chennai","Citny","Seoul","Tokoyo","Beijing"]

if("location" in jsonObj):
    if(user_location is not None and isinstance(user_location,dict)):
       user_country = jsonObj.get("location").get("country");
       if "country" in jsonObj.get("location", {}):
           if(not user_country=="" and user_country in Country and isinstance(user_country,str)):
             isCountry = True
       else:
        print("location.country key not found or given dictionary type")
        
        user_city = jsonObj.get("location").get("city");
        if "city" in jsonObj.get("location",{}):
            if(not user_city=="" and user_city in City and isinstance(user_city,str)):
                 isCity = True
        else:
            print("location.city key not found or given dictionary type")
    
        if(isCountry==True and isCity==True):
          print("user_location successfully added")
        else:
          print("Enter correct location.country,location.city values.")
    else:
        print("location value is wrong")
else:
    print("location key is not found")
    
user_personal = jsonObj.get("personal_status")

isRole = False;
isBatting = False;
isBowling = False;
isScore = False;
isWicket = False;

role = ["Batsman","Bowler","WK"]
Batting_style = ["Right-hand","Left-hand"]
Bowling_style = ["Right-Arm-Fast","Right-Arm-Slow","Left-Arm-Fast","Left-Arm-Slow","Off-spin","Leg-break"]

if("personal_status" in jsonObj):
    if(user_personal is not None and isinstance(user_personal,dict)):
        user_role = jsonObj.get("personal_status").get("role")
        if "role" in jsonObj.get("personal_status",{}):
            if(not user_role=="" and isinstance(user_role,str) and user_role in role):
               isRole = True
            else:
              print(f"Enter correct role in {role}")
        else:
             print("role key is not found.")
 
        user_batting = jsonObj.get("personal_status").get("batting_style")
        if "batting_style" in jsonObj.get("personal_status",{}):
          if (not user_batting=="" and isinstance(user_batting,str) and user_batting in Batting_style):
            isBatting = True;
          else:
            print(f"Enter correct batting_style in {Batting_style}")
        else:
          print("batting_style key is not found.")
        
        user_bowling = jsonObj.get("personal_status").get("bowling_style")
        if "bowling_style" in jsonObj.get("personal_status",{}):
              if (not user_bowling=="" and isinstance(user_bowling,str) and user_bowling in Bowling_style):
                isBowling = True;
              else:
                print(f"Enter correct bowling_style in {Bowling_style}")
        else:
             print("bowling_style key is not found.")
        
        user_hs = jsonObj.get("personal_status").get("highest_score")
        if "highest_score" in jsonObj.get("personal_status",{}):
                if (not user_hs<0 and isinstance(user_hs,int)):
                    isScore = True
                else:
                   print(f"Enter positive number score")
        else:
            print("highest_score key is not found.")
   
        user_wicket = jsonObj.get("personal_status").get("wickets_taken")
        if "wickets_taken" in jsonObj.get("personal_status",{}):
                if (not user_wicket<0 and isinstance(user_wicket,int)):
                    isWicket = True
                else:
                   print(f"Enter positive number wickets")
        else:
          print("wickets key is not found.")
    
        if(isRole==True and isBatting==True and isBowling==True and isScore== True and isWicket == True):
          print("Successfully added personal_status")
        else:
          print("Failed add to personal_details")    
    else:
        print("personal_value is wrong") 
else:
    print("personal_status key is not found.")