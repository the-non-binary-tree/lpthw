name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on his coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Drill
INCHES_TO_CENTIMETERS = 2.45
# POUNDS_TO_KILIGRAMS = 2.205
POUNDS_TO_KILIGRAMS = 0.4 
height_in_metric = height * INCHES_TO_CENTIMETERS #centimeters
weight_in_metric = weigth * POUNDS_TO_KILIGRAMS #kilograms
print(f"Height in metric is {height_in_metric} centimeters.")
print(f"Weight in metric is {weight_in_metric} kilograms."
