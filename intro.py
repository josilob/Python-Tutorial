# Python uses snake_case with underscore as word separator
# To execute code type: 'python3 filename.py'

# Variables:
int_price = 10
float_price = 10.0
string_price = '10'
is_free = False
#print(int_price, float_price, string_price, is_free, not is_free)

# Variable conversion
# int to float
# print(float(int_price))
# float to int
# print(int(float_price))
# string to int
# print(int(string_price))
# int to string
# print(type(str(int_price)))  # prints <type 'str'>

# Capturing user input
#my_name = input('Type your name: ')
# print('Hi '+my_name)

# Strings

course = "Python's course for beginners"  # DBL && Single combo
course = '''Multiline
string with three apostrophes'''
course = 'Python for beginners'  # single quoted string
# print(course[0])  # first char 'P'
# print(course[-1])  # last char 's'
# print(course[0:3])  # first 3 characters (0 inclusive, 3 exclusive) 'Pyt'
# omitting first element is set by default to 0, while second element is replaced with last element
# print(course[0:])  # from 0 to string's length (whole string)
# print(course[:5])  # first 5 characters
name = 'Jennifer'
# print(name[1:-1])  # => 'ennife'

# Formatted Strings
first = 'John'
last = 'Doe'
message = first + ' [' + last + '] is a coder'
# print(message)  # => John [Doe] is a coder
msg = f'{first} [{last}] is a coder'
# print(msg)  # => Same output

# String methods

course = 'Python for beginners'
print(len(course))
print(course.upper())  # => Does not modify current string
print(course.lower())  # => Does not modify current string

# Case sensitive find method that returns first index of string occurence or -1
print(course.find('Pyt'))  # => 0
print(course.find('o'))  # => 4
print(course.find('x'))  # => -1
print(course.replace('beginners', 'absolute beginners'))

# Check for existance of character or sequence in a string
print('Python' in course)  # => True

print(course.capitalize())  # => Capitalizes first letter of a string
print(course.title())  # => Capitalizes first letter of each word in a string
