# for loops
print("Counting from 1 to 5")
for i in range(1, 6):
    print(i)


print("Reversed counting from 5 to 1")
for i in range(5, 0, -1):
    print(i)

# while loop
count = 1
print("While Loop")
while count <= 5:
    print(count)
    count += 1

count = 5
print("Reversed while loop")
while count >= 1:
    print(count)
    count -= 1

# loops with enumerate
fruits = ["apple", "banana", "cherry"]
print("fruit with indices")
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')
