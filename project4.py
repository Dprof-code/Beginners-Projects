# This program can convert dollars to naira
# In coming updates it would be able to convert from one currency to another currency
# $1 is currently #380
import time
dollar = input("Enter the amount in dollars: $")
time.sleep(1)
print("wait while I convert it")
time.sleep(3)
naira = int(dollar) * 380
naira = str(naira)
print("$" + dollar + " is currently " + "#" + naira)
