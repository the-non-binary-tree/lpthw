from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("the script is called:", script)
print("Your first variable is", first)
print("Your second variable is", second)
print("Your third variable is", third)

fourth = input("Give one more variable: ")
print("Your fourth variable is", fourth)

# Drill
# ValueError: not enough values to unpack (expected 4, got 1)
