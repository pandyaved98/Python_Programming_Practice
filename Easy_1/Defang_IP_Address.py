#Write a program to Defang the IP Address.
import os

#Define a function to get the IP Address from user.
def get_ip_address():
    ip_address = input("Please enter the IP Address: ")
    return ip_address
    print("IP Address: " + str(ip_address))

#Use the user input and defang it with [.]
def defang_ip_address(ip_address):
    defanged_ip_address = ip_address.replace(".", "[.]")
    return defanged_ip_address
    print(defanged_ip_address)
