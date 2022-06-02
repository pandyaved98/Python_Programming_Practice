#Import the getpass module to verify the Password stored in Dictionary
import getpass

#Create a dictionary with Key-Value Pair
database = {"vedant.pandya": "123456", "pandya.vedant": "654321", "ved.pandya": "654321", "ved.pandya":"123456"}

#Get Username from user
username = input("Enter Your Username : ")

#Enter the password if the user found in the Database
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")
