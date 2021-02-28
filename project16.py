courseName12 = input("Enter the course name ")
score12 = int(input("Enter score "))
CU12 = int(input("Enter the Credit Unit: "))

F = int(0)
D = int(2)
C = int(3)
B = int(4)
A = int(5)

if score12 <= 44:
    GP1 = F * CU12
elif score12 <= 49:
    GP1 = D * CU12
elif score12 <= 59:
    GP1 = C * CU12
elif score12 <= 69:
    GP1 = B * CU12
elif score12 <= 100:
    GP1 = A * CU12

# I want this program to accept to accept scores of users, so if their score is between 70 - 100, then GP1 should be
# equal A*CU12, if their score is between 60 - 69, then GP1 should be
# # equal to B*CU12, if their score is between 50 - 59, then GP1 should be
# # equal to C*CU12, if their score is between 45 - 49, then GP1 should be
# # equal D*CU12, if their score is between 0 - 44, then GP1 should be
# # equal F*CU12, I want to out put value of GP1#
