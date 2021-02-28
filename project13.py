# This program is available for store keeping validation
# It receives input from the user and stores it in the store database

shop_data = {}
user_name = input("Please enter your name: ")
print("Hi " + user_name + ",nice having you here")
product_name = input("Enter the name of the product: ")
product_price = input("Enter the price of the product: ")
shop_data = {product_name: product_price}

product_name2 = input("Enter the name of the product: ")
product_price2 = input("Enter the price of the product: ")
shop_data = {product_name: product_price, product_name2: product_price2}

product_name3 = input("Enter the name of the product: ")
product_price3 = input("Enter the price of the product: ")
shop_data = {product_name: product_price, product_name2: product_price2, product_name3: product_price3}

product_name4 = input("Enter the name of the product: ")
product_price4 = input("Enter the price of the product: ")
shop_data = {product_name: product_price, product_name2: product_price2, product_name3: product_price3, product_name4: product_price4}


product_name5 = input("Enter the name of the product: ")
product_price5 = input("Enter the price of the product: ")
shop_data = {product_name: product_price, product_name2: product_price2, product_name3: product_price3, product_name4: product_price4, product_name5: product_price5}

print(shop_data)

print("You can now search for goods in stock")
user_search = input("Enter a product name: ")

if user_search in shop_data:
    print(user_search + " is available")
else:
    print("check back later " + user_search + " is not in stock")
