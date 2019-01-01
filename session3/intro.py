#yob_str = input("Your year of birth?")
#if not yob_str.isdigit():
#   print("not a number")
#else:
#    yob = int(yob_str)
#    age = 2018 - yob
#    print(age)

#yob_str = input("Your year of birth?")
#while not yob_str.isdigit():
 #   print("Not a number, enter again")
 #   yob_str = input("your year of birth?")
#yob = int(yob_str)
#age = 2018 - yob
#print(age)



loop = True
while loop:
    pwd = (input("Enter your password: "))
    loop = False #assume password is valid
    if len(pwd) < 8:
        print("Password length must be greater than 8")
        loop = True
    if not pwd.isalnum():
        print("Password must not contain special characters")
        loop = True
    if not pwd.isdigit():
        print("Password must contain letters")
        loop = True
    if not pwd.isalpha():
        print("Password must contain digits")
        loop = True
        
print("password OK")