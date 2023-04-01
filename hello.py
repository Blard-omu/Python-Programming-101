#Installations and downloading of extensions
#Extensions for Vscode -Python (Pylance), Python indent, python test explorer, Prettier
#Python syntax
#Indentation
# def hello():
#     print("Hello world!")


#Python Variables
# variables are used to store data
# variable name cannot start with num, other characters except underscore _ 
# there shouldn't be space in btw a variable name
name = "Debby"
age = 43
is_active = True
gravity = 9.81

print(type(name), name)
print(type(age), age)
print(type(is_active), is_active)
print(type(gravity), gravity)

print("My name is " + name + " and " + str(age) + " years old" + " and I am very active student")


#Python Data-types-

'''
1)String Type 
2)Number Type (int, float, complex)
3)Boolean Type (bool)
4)Sequence Type (list, sets, tuple, range)
5)Mapping Type (Dictionary i.e dict)
'''

# Strings
# String methods index, len, upper, lower, slice, endwith, startwith, replace, capitalize, title
# String formatting

string1 = 'My string'
string2 = "My second string"
my_str = str(90)
print(type(my_str), my_str)

# len()
a = len(string1)
print(a)
print(len(string2))
print(len(my_str))

# upper()
# print((string1).upper())
# print((string2).lower())
# print((string2).capitalize())
# print((string2).title())
# print((string2))
edited_str2 = string2.replace("second", "third")
# print((edited_str2))

# string formatting f
# str_format = f'My name is {name} I\'m {age} years old'
str_format = f"My name is {name} I'm {age} years old"
# print(str_format)


print("/////////Number data type //////////")
# Number Data type int, float, complex
n = 23
BMI = 5.98
complex_num = 3j + 5
print(type(n), n)
print(type(BMI), BMI)
print(type(complex_num), complex_num)

print(n*2)

print("///////Booleans/////////")
# Booleans True, False
print(bool(5>3))
# print(bool(n == BMI))
print(bool(n > BMI) and bool(n != 0))
print(bool(n > BMI) and bool(n < 0))
print(bool(n > BMI) or bool(n < 0))
print(bool(n > BMI) and bool(n >= 0))

print("//////Operators/////")
# OPERATORS arithmetic, assignment,comparison, logical
# Arithmetic + - * / // ** %
# print(5-3+8/6)
# print(3 ** 4)
# print(40 % 6)
# print(20/3)
# print(20//3)

# Assignment operators =, +=, -=, *=, /=
a = 4
b = 10
c = 8

# a = a + 3
a += 3
# a = a - 2
a -= 2
b += a
b *= b

print(a)
print(b)

print("//////////Comparison operators//////////")
# Comparison Operators ==, !=, <, >, <=, >=
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)



print("//////////Logical Operators////////")
# Logical Operators and, or , not
print((a == b) and (a >= b))
print((a != b) and (a >= b))
print((a != b) or (a >= b))
print((a == b))
print(not (a == b))
