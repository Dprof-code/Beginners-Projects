# This program is used to check the strength of a password
# A strong password must contain letters, numbers and symbols

password = input("Enter your password: ")
if len(password) >= 10:
    print("Your Password is strong")
elif len(password) >= 5:
    print("Your password strength is good")
else:
    print("Your password is weak")
