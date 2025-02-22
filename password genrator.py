import random
print("------------------------------------")
print("Welcome to the password generator!")
print("------------------------------------")
platform=input("Enter which platform the password is generated for: ")
length=int(input("Enter the length of a password : "))
cp=platform.capitalize()
number='1234567890'
loweralph="abcdefghijklmnopqrstuvwxyz"
upperalph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialsym="~!@#$%^&*"

sp=list(specialsym) 
lo=list(loweralph)
up=list(upperalph)
num=list(number)

finalpass=lo+up+num+sp

shuff=random.sample(finalpass,length)
proper="".join(shuff)
print("Password is : ",proper)




