"""
# Part1
username = "iremcaliskan"
password = "irem123"

tempUsername = input("Username: \n")
tempPassword = input("Password: \n")

if tempUsername == username and tempPassword == password:
    print("Login is successful. You are redirecting to the Home page...")
elif tempUsername == " " or tempPassword == " ":
    print("Fill the blank fields!") 
elif tempUsername != username and tempPassword == password:
    print("Your username is incorrect!") 
elif tempUsername == username and tempPassword != password:
    print("Your password is incorrect!") 
elif tempPassword != password and tempUsername !=username:
    print("Username and password not found in the system!")
else:
    print("Something went wrong!")

"""

# Part2 - Extra
myDictionary = {"username":"iremcaliskan", "password":"irem123"}

username = myDictionary.get("username")
password = myDictionary.get("password")

dicUserName = input("Username: \n")
dicPassword = input("Password: \n")

myDictionaryComing = {}
myDictionaryComing["username"] = dicUserName
myDictionaryComing["password"] = dicPassword

if dicUserName == username and dicPassword == password:
    print("Login is successful. You are redirecting to the Home page...")
elif dicUserName == " " or dicPassword == " ":
    print("Fill the blank fields!")
elif dicUserName != username and dicPassword == password:
    print("Your username is incorrect!") 
elif dicUserName == username and dicPassword != password:
    print("Your password is incorrect!") 
elif dicPassword != password and dicUserName !=username:
    print("Username and password not found in the system!")
else:
    print("Something went wrong!")