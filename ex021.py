def add(a, b):
  print(f'ADDING {a} + {b}')
  return a + b

def subtract(a, b):
  print(f'SUBTRACTING {a} - {b}')
  return a - b

def multiply(a, b):
  print(f'MULTIPLYING {a} * {b}')
  return a * b

def divide(a, b):
  print(f'DIVIDING {a} / {b}')
  return a / b

print('Let\'s do some math with just functions!')

age = add(20, 9)
height = subtract(50, 1)
weight = multiply(50, 2)
iq = divide(0, 5)

print(f'Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}')

print('Here is a puzzle.')

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print('That becomse: ', what, 'Can you do it by hand?')
