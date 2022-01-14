# Arithmetic Operations
print(10+3)  # Addition
print(10-3)  # Subtraction
print(10*3)  # Multiplication
print(10/3)  # Division => 3.3333333333333335
print(10//3)  # Integer Division => 3
print(10 % 3)  # Remainder
print(10 ** 3)  # Exponent

# Augmented asignment operator
x = 10
x = x+3
print(x)
x += 3
print(x)  # => Incremented by 3 (same as x = x + 3)

# Operator precedence

x = 10 + 3 * 2
print(x)  # => yields 16 as 10+(3*2)
# Parentheses > Exponentiation > Multiplication/Division > Addition/Subtraction
x = (2+3)*2**2  # => 5 * 4 = 20
