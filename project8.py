# This python program is for form validation
name = input("Enter your name: ")
if len(name) < 3:
    print("Name too short! must be at least 3 characters")
elif len(name) > 50:
    print("Name too long! max of 50 characters")
else:
    print("Name looks good!")
