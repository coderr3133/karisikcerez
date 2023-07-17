import random
import string
def generate(lenght):
    password = ""
    for i in range(int(lenght)):
        password += random.choice(string.ascii_letters+string.digits+"!"+"<"+">"+"#"+"+"+"&"+"/"+"="+"?"+"*"+"-"+"_")
    return password
choose = input("""       Hello!
[1] See Your Passwords
[2] Add a Password
[3] Generate a new Password\n""")
if choose == "1":
    with open("ps.txt", "r") as file:
        print(file.read())
elif choose == "2":
    name = input("Name: ")
    passwrd = input("Password: ")
    with open("ps.txt", "a") as file:
        file.write(name+": "+passwrd+"\n")
        

elif choose == "3":
    name = input("Name: ")
    lenght = input("lenght(enter a number pls):")
    with open("ps.txt", "a") as file:
        file.write((name)+": "+(generate(lenght))+"\n")
    print("Your password is successfully saved '"+generate(lenght)+"'")


else:
    print("Please make sure you writed it right")