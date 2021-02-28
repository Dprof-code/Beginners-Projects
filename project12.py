# This program is a weight converter
weight = input("Weight: ")
weight = int(weight)
print("Select your weight unit below")
weight_unit = input("(L)bs or (K)g: ")
if weight_unit == "K":
    weight_kg = weight * 2.205
    weight_kg = str(weight_kg)
    print("You weigh " + weight_kg + " kilos")
elif weight_unit == "L":
    weight_lbs = weight / 2.205
    weight_lbs = str(weight_lbs)
    print("You weigh " + weight_lbs + " pounds")
else:
    print("Invalid input!")
print("That's the end of the program, thanks for been here!")
