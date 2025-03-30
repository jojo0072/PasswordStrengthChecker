import getpass
import string
import os

def main():
    print("Password-Strength-Checker")
    while True:
        pw=getpass.getpass("Enter your password: ")
        if all(char==" " for char in pw):
            print("Invalid Input!")
        else:
            break
    check_pw(pw)  
    again=input=("Check another password (y/n): ")
    while again =="y":
        os.system("clear")
        main()
    else:
         exit()   
def check_pw(pw):
    categories=[0, 0, 0, 0, 0, 0]
    for c in pw:
        if c in string.ascii_lowercase:
            categories[1]+=1
        elif c in string.ascii_uppercase:
            categories[2]+=1
        elif c in string.digits:
            categories[3]+=1
        elif c == " ":
            categories[4]+=1
        else:
            categories[5]+=1
 
    strength, lowercase, uppercase, digits, whitespace, special=categories
    for n in categories:
        if n >=1:
            strength+=1
    remarks={1: "Your password is weak. Consider adding more variety of characters.", 2: "Your password is fair, but could be stronger with additional character types." , 3: "Your password is moderate. Adding more characters and variety would improve its strength.",4: "Your password is strong! It contains a good mix of characters, but adding a few more would make it even better.", 5: "Congratulations! Your password is really strong and secure. Keep it safe and don't forget it!"}        
    print("\nYour password has: ")
    print(f"- {lowercase} lowercase letters")
    print(f"- {uppercase} uppercase letters")
    print(f"- {digits} digits")
    print(f"- {whitespace} whitespaces")
    print(f"- {special} special characters")
    print(f"\nRemarks: {remarks[strength]} ")
    print(f"Strength score: {strength}/5")      
main()                                                                                                                                                                                                                       