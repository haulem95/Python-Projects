import random
import math
import datetime
import os
import sys
import time

# random
random_number = random.randint(1, 10)
print(random_number)

# choose a random element from a list

fruits = ['apple', 'orange', 'cherry', 'banana']

random_fruit = random.choice(fruits)
print(random_fruit)

# shuffle the list

random.shuffle(fruits)
print(fruits)

# math

print(math.pi)
print(math.sqrt(16))
print(math.floor(4.7))
print(math.ceil(5.3))
print(math.pow(5, 3))

pi = 3.141592654343
print(round(pi, 2))  # round to 2 decimal places

# datetime
current_time = datetime.datetime.now()
print(f'Current date and time: {current_time}')
print(f"Today's date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().year}")

# OS module
current_directory = os.getcwd()
print(current_directory)
print(f"List of the files: {os.listdir('.')}")

# Sys module
print(f"Python Version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Python Version: {sys.version_info}")
