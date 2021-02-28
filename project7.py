price = 1000000
ten_percent = price - 10/100 * price
ten_percent = str(ten_percent)
twenty_percent = price - 20/100 * price
twenty_percent = str(twenty_percent)
buyer_credit = False
if buyer_credit is True:
    print("The cost of the house is " + "$" + ten_percent)
else:
    print("The cost of the house is " + "$" + twenty_percent)

# solution
price = 1000000
has_good_credit = False
if has_good_credit is True:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
    print(f"Down payment: ${down_payment}")
