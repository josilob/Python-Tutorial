# ARITHMETIC OPERATIONS
import math
print(10+3)  # Addition
print(10-3)  # Subtraction
print(10*3)  # Multiplication
print(10/3)  # Division => 3.3333333333333335
print(10//3)  # Integer Division => 3
print(10 % 3)  # Remainder
print(10 ** 3)  # Exponent

# Augmented asignment operator
x = 10
x = x+3  # value incremented normally
print(x)  # => 13
x += 3  # =>16
print(x)  # => Incremented by 3 (same as x = x + 3)

# OPERATOR PRECEDENCE
x = 10 + 3 * 2
print(x)  # => yields 16 as 10+(3*2)
# Parentheses > Exponentiation > Multiplication/Division > Addition/Subtraction
x = (2+3)*2**2  # => 5 * 4 = 20

# MATH FUNCTIONS
x = 2.9
print(round(x))
print(round(2.5))  # => 2
print(abs(-x))

# For more complex mathematical calculations, we import modules
# This way we keep code compartmentalized
# 'import math' on top of the file, which is now an object whose methods we can access
print(math.ceil(2.9))
print(math.floor(2.9))
