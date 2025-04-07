x = 10
y = 5
# basic operations
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % y)  # modulus
print(x**y)  # exponentiation

x += 5  # same as x = x + 5
print(x)

# string concatenation
first_name = "Hayou"
last_name = "Lemessa"
full_name = first_name + ' ' + last_name
print(full_name)
print('my first name is', first_name, 'and my last name is', last_name)
# same as above.
print(f"Hey my name is {first_name} and my last name is {last_name}")

# int floor division
a = 17
b = 5
print(a/b)
print(a//b)  # rounded down

i, j, k = 1, 2, 3
print(i, j, k)

# swapping values

m = 10
n = 20
m, n = n, m  # swapping syntax
print(n)
print(m)

# comparison operations
c = 5
d = 10
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c <= d)
print(c >= d)

# logical operators'
e = True
f = False

print(e and f)
print(e or f)
print(not f)
print(not e)

# string slicing

text = 'python programming'
print(text[0:6])  # from index 0 to 5, 6 is excluded
print(text[7:10])  # from index 7 to 9, 10 is excluded
print(text[::-1])  # from the end to the start, step -1, reversing string


# string formatting with .format()