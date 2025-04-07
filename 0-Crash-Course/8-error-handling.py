try:
    number = int(input("Enter a number: "))
    result = 10/number
    print(result)
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("you can't divide by zero")
finally:
    print("This piece of code will always run")
