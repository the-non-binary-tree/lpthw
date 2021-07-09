types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# 2 string variables in a string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# String variable in a string
print(f"I said: {x}")
# String variable in a string
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# 2 string variables in a string
print(w + e)

# Drill

# When concatenate with the '+' sign, the operation will fail if the operand follows the plus sign is not a string even if if implements the __str__ method
