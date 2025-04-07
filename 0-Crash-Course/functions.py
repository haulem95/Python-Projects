# Functions are blocks of code that can be reused, they can take arguments and return values.
def greet_everyone():
    print("Hello, everyone!")


greet_everyone()


def greet(name):
    print("Hello", name)


greet('Hayou')
greet('Kyle')


user1 = "Emma"

print("Hello", user1, "Welcome to our app")
print("We hope you enjoy using our services.")
print("Let us know if you need any help.")

user2 = "Esther"

print("Hello", user2, "Welcome to our app")
print("We hope you enjoy using our services.")
print("Let us know if you need any help.")

user3 = "John"

print("Hello", user3, "Welcome to our app")
print("We hope you enjoy using our services.")
print("Let us know if you need any help.")

# same as above but easier because of the existence of functions.


def greet_user(name):
    print('Hello,', name, ' Welcome to our app')
    print("We hope you enjoy using our services.")
    print("Let us know if you need any help.")


greet_user("emma")
greet_user('Jane')
greet_user('John')


def power(base, exponent):
    return base ** exponent


x = power(2, 3)
print(x)
print(power(4, 5))
