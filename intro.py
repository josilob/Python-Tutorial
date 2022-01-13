# Python uses snake_case with underscore as word separator
# To execute code type: 'python3 filename.py'

# Variables:
int_price = 10
float_price = 10.0
string_price = '10'
is_free = False
print(int_price, float_price, string_price, is_free, not is_free)

# Variable conversion
# int to float
print(float(int_price))
# float to int
print(int(float_price))
# string to int
print(int(string_price))
# int to string
print(type(str(int_price)))  # prints <type 'str'>

# Capturing user input
my_name = input('Type your name: ')
print('Hi '+my_name)
