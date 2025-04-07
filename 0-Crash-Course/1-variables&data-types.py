print("Hello, World!")

# strings
name = 'Alex'

# integers
age = 25

# float
height = 1.82

# boolean

is_student = False

print("Hey, my name is " + name)
print("I am", age, "years old")

print(name[-1])

message = 'hello world'

print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace('l', "L"))
print('World' in message)  # prints false coz case sensitive
print(len(message))

greeting1 = "Hello"
greeting2 = "hello"

if greeting1 == greeting2:
    print('they are the same')
else:
    print('they are different')

# type conversions

age_str = "30"
age_num = int(age_str)
print(type(age_str))
print(type(age_num))

# rounded back to the smallest integer regardless to rounding rules of maths.
price_float = 29.99
price_int = int(price_float)

print(price_int)
print(type(price_float))
print(type(price_int))
