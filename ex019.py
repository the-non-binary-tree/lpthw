def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f'You have {cheese_count} cheeses!')
  print(f'You have {boxes_of_crackers} boxes of crackers!')
  print('That\' enough for a party!')
  print('Get a blanket.\n')
  
print('We can just give the function numbers directly:')
cheese_and_crackers(20, 30)

print('OR, we can user variables from our script:')
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print('We can even do math inside too:')
cheese_and_crackers(10 + 20, 5 + 6)

print('And we can combine the two, variables and math:')
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)


def my_function(my_argument):
  print(f'This is my argument {my_argument}')
  
my_function(486)

my_argument = '974'
my_function(my_argument)

my_function(my_argument * 10)

my_function(input('Your argument: '))

my_function(5 + 3)

my_function([5, 3])
