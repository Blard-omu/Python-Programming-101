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
4)Collection Data type (list, sets, tuple, range)
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



print("////////List//////////")
# Python Collections list, tuple, set and dictionary
# List
# List is a collection of items in rectangular bracket. list items are ordered, changeable
lst1 = list()
print(type( lst1))
lst = [2, "string", True, 9.8, 48, [1, 4]]
print(type(lst))
first_item = lst[0]
sec_item = lst[1]
print(first_item)
print(sec_item)
# last_item = lst[-1]
last_item = lst[5]
print(last_item)
print(lst[5][1])


# len()
print(len(lst))

print(lst)

# Append
lst.append("apple")
lst2 = ["Blard", "Python"]

print(lst)
lst.extend(lst2)
print(lst)

# slicing
# lst[start:end:step]
sliced_lst = lst[4:7]
print(sliced_lst)
print(lst[::2])

lst.insert(2, "inserted")
print(lst)

# pop
# lst.pop()
# print(lst)
# lst.pop(2)
# print(lst)

# clear
# lst.clear()
# print(lst)

# del
# del lst
# print(lst)

# for item in lst:
    # print(f'Item {item}')
    

my_car = ['Volvo', 'Toyota', 'Honda', 'Ford', 'Mercedes', 'BMW']

fav_cars = my_car[0:5:4]
# print(fav_cars)
# print(my_car[1::2])

# for car in my_car:
    # print(f'My favorite car is {car}')



# Tuples
# Tuple is immutable
# Items are ordered
# NB: When tuple is created, you can not add, remove, replace or reorder items

# creating tuples
tpl = tuple([2, "string"])
print(type(tpl), tpl)
my_tpl = ("string", 2, 9.6)
print(type(my_tpl), my_tpl)
print(my_tpl[0])
print(my_tpl[1])
# print(my_tpl[2])

# max, min, len, sum
print(len(tpl))
print(len(my_tpl))
# print(max(my_tpl))

# slicing tuple
print(my_tpl[0::2])

print("string" not in tpl or "string" in my_tpl)

new_tpl = list(tpl)
print(type(new_tpl), new_tpl)
new_tpl.insert(0, "new-item")
print(new_tpl)
modified_tpl = tuple(new_tpl)
print(type(modified_tpl), modified_tpl)


# Sets
# Set is a collection of unordered items enclosed in a curly brackets { }

math_set = set(['ruler', 'pencil', 'compass', 'divider', 'eraser', 'sharpener', 'pencil'])
print(math_set)
print(type(math_set))
print(len(math_set))

my_set = { "item1", "item2", "item3", "item4"}
print(type(my_set), my_set)
# for item in math_set:
#     print(item)


# dictionary
# dictionary is a collection of unordered items in key-value pairs.
# dictionary mutable (modifiable)
my_dict = dict()
print(type(my_dict))
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(dct)

person = {
    'first_name': 'blard',
    'last_name': 'Omu',
    'age': 36,
    'country': 'United States',
    'skill': ['Javascript', 'React', 'Python', 'Django', 'Node'],
    'address': {'street': 'stella'},
    'city': 'lagos'
}

# len
print(person)
print(len(person))

# Accessing dict
print(person['address'])
print(person['country'])
print(person['age'])
print(person['skill'])

# get()
print(person.get('country'))
print(person.get('first_name'))
print(person.get('city'))

# keys() and values()
print(person.keys())
# print(person.values())

# modifying dictionary
person['age'] = 30
# print(person['age'])
# update()
# person.update({'name': 'John'})
# print(person['name'])
# print(person)

# Removing item
# print(person.pop('name'))
# print(person)

# items()
# print(person.items())

# for key, value in person.items():
#     print(f'The key is {key} and the value is {value}')


# print('name' in person)
# print('city' in person)

# clear()
person.clear()
# print(person)

# delete 
del person
# print(person)

# Conditionals if, if-else, elif, break, continue

# if
# syntax
# if condition:
#     run this code
a = 3
# if a > 0:
#     print('a is a positive number')
    
    
# if-else
# syntax
# if condition:
#     run this code
# else:
#     do something different

if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
    

# if elif else
# if condition1:
#     do this
# elif condition2:
#     do this:
# elif condition3:
#     do this:
# else:
#     do this

if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')




