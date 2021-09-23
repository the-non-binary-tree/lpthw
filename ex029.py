people = 20
cats = 30
dogs = 15

if people < cats:
  print("Too many cats! The world is doomed!")
  
if people > cats:
  print("Not many cats! The world is saved!")
  
if people < dogs:
  print("The world is drooled on!")
  
if people > dogs:
  print("The world is dry!")
  
 
dogs += 5

if people >= dogs:
  print("People are greater than or equal to dogs.")
  
if people <= dogs:
  print("People are less than or equal to dogs.")
  
if people == dogs:
  print("People are dogs.")

#Drill
#What if does to the code under it:
# # The IF statement is a decision-making statement 
# # that guides a program to make decisions based on 
# # specified criteria. The IF statement executes 
# # one set of code if a specified condition is met (TRUE) 
# # or another set of code evaluates to FALSE.
#Why the code under if needs to be indented four spaces:
# # in Python, it is required for indicating what 
# # block of code a statement belongs to
#What happens if it isn't indented:
# # Depends on the actual code, but basically it will 
# # be executed regardless of the value of the expressions
# # following the if statements
#What happens if change the initial values of variables:
# # The expressions in the if statements will validate to different values
