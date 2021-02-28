# This program asks for users weight in pounds and converts it to kilograms, then output it
# 2.205 pounds makes 1 kg
weight_in_pounds = input("Enter your weight in pounds: ")
weight_in_kg = float(weight_in_pounds) / 2.205
weight_in_kg = str(weight_in_kg)
print("You weigh " + weight_in_kg + "kg")
