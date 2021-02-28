# This program is used to measure the eligibility status of loan applicants
income = input("Enter your annual income in multiples of 1000: ")
income = int(income)
rating = input("Enter credit ratings in percentage: ")
rating = int(rating)
if income <= 50000 and rating <= 30:
    print("I am sorry, you are not eligible for a loan")
elif income <= 50000 and rating > 30:
    print("You are eligible for loan up to #100,000")
elif income > 50000 and rating > 30:
    print("You are eligible to receive a loan")
else:
    print("INVALID INPUT!!!")
