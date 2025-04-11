print("📝 Character Type Checker 📝")
character = input("Enter a single character: ")

if character.isalpha():
    print("This is a letter")
elif character.isdigit():
    print("This is a number")
else:
    print("This is a special character.")
