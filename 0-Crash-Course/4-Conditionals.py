# python uses identation to define blocks of code and not curly braces other symbols.

temp = 28
if temp > 30:
    print("It's hot outside")
elif temp > 20:
    print("It's warm outside")
else:
    print("It's cold outside")


# checking multiple conditions with logical operators

age = 25
has_license = True

if age >= 18 and has_license:
    print('You can drive a car')
elif age >= 18 and not has_license:
    print('You need a license to drive')
else:
    print('You are underage to drive and you need a fucking license.')


# nested conditionals

score = 85

if score >= 60:
    print("You have passed")
    if score >= 90:
        print("You got an A")
    elif score >= 80:
        print("You got a B")
    elif score >= 70:
        print("You got a C")
    else:
        print("You got a D")
else:
    print("You failed")

# using the 'in' operator in conditionals

fruit = 'apple'
if fruit in ['apple', 'banana', 'orange']:
    print(f"{fruit} is in the list")

# Ternary operator (one-line if-else)
age = 20
status = 'adult' if age >= 18 else 'minor'
print(f'status: {status}')


# comparing strings
password = 'secret123'

if password == 'secret123':
    print("Access Granted")
else:
    print("Access Denied")

# chaining comparison

x = 15

if 10 < x < 20:
    print("x is between 10 and 20")


# truthy or falsy value

user_input = ''

if user_input:
    print("Input Provided")
else:
    print('Provide input bitch!')
