import json

user_data = {
    "name": "johndoe",
    "email": "johndoe123@gmail.com",
    "age": 30,
    "gender": "Male",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    },
    "phone_numbers": [
        {"type": "home", "number": "9457834875"},
        {"type": "work", "number": "8458745345"}
    ]
}

user_name = user_data.get("name")

if("name" not in user_data):
    print("name key is not found")
    
elif(not isinstance(user_name, str) or user_name == "" or not user_name.isalpha()):
    print("name value is required")
    
else:
    print("name validation will success")
    
user_email = user_data.get("email")

if("email" not in user_data):
    print("email key is not found")
    
elif(user_email=="" or not isinstance(user_email,str)):
        print("email value is required")
else:
    print("email validation will success")
    
user_age = user_data.get("age")

if("age" not in user_data):
    print("age key is not found")
    
elif(user_age==0 or not isinstance(user_age,int) or (user_age < 18 or user_age>120)):
        print("age value is required")
else:
    print("age validation will success")
    
user_gender = user_data.get("gender")

if("gender" not in user_data):
    print("gender key is not found")
    
elif(user_gender=="" or user_gender not in ["Male", "Female", "Other"]):
        print("gender value is required")
        
else:
    print("gender validation will success")
    
user_address = user_data.get("address")
user_address_street = user_data.get("address").get("street")
city = user_data.get("address").get("city")
user_address_city = city.replace(" ","")
user_address_state = user_data.get("address").get("state")
user_address_zip = user_data.get("address").get("zip")

if(user_address is not None):
   if(user_address_street is None):
      print("street key is not found")
   elif(user_address_street=="" or not isinstance(user_address_street,str)):
        print("street value is required")
   else:
        
        if(user_address_city is None):
           print("city key is not found")
        elif(user_address_city=="" or not isinstance(user_address_city,str) or not user_address_city.isalpha()):
           print("city value is required")
        else:
           

           if(user_address_state is None):
               print("state key is not found")
           elif(user_address_state==""or not isinstance(user_address_state,str) or not user_address_state.isalpha()):
               print("state value is required")
           else:
             
                if(user_address_zip is None):
                   print("zip key is not found")
                elif(user_address_zip=="" or not user_address_zip.isdigit()):
                   print("zip value is required")
                else:
                    print("address validate will be success")
else:
    print("address key is not found")
    
user_phone = user_data.get("phone_numbers")
isType = False
isNumber = False
if(user_phone is not None):
   for i in range (0,len(user_phone)):
    type = user_phone[i].get("type")
    number = user_phone[i].get("number")
    if(type=="home" or type=="work"):
        isType = True
    if(number.isdigit() and len(number)==10):
         isNumber = True
         
     
    if(isType==True and isNumber==True):
        print("phonenumber validate will be success",type)
    else:
        print("type or number is required")
    
else:
     print("phone number key in not found")
     

