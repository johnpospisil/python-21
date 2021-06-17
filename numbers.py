from math import *
import random
import secrets
import numpy as np

# Numbers can be printed directly
my_number = 20
print(my_number)
print(-3.14159)
print("")

# Numbers need to be converted to strings to be concatenated with strings
print("String contatenated with a number: " + str(20))
print("")

# Modulus Operator - i.e. the remainder of division
print("10 modulus 3 = " + str(10 % 3))
print("10 / 3 without remainder = " + str(10 // 3))
print("")

# Common Math functions
print("Absolute value of -10: " + str(abs(-10)))
print("2^10 = " + str(pow(2, 10)))
print("2^10 = " + str(2 ** 10))
print("The larger of 4 and 5 is " + str(max(4, 5)) + ".")
print("The smaller of 4 and 5 is " + str(min(4, 5)) + ".")
print("3.14159 rounded is " + str(round(3.14159)) + ".")
print("")

# Common Math Library functions
print("The floor of 3.7 is " + str(floor(3.7)) + ".")
print("The ceiling of 3.7 is " + str(ceil(3.7)) + ".")
print("The sqrt of 36 is " + str(sqrt(36)) + ".")
print("")

# RANDOM NUMBERS
print(f'Randon number 0-1: {random.random()}')
print(f'Random number 1-10: {random.uniform(1, 10)}')
print(f'Random integer 1-10: {random.randint(1, 10)}')
print(f'Random integer 1 <= n < 10: {random.randrange(1, 10)}')
print(f'Random value from mean=0, std_dev = 1: {random.normalvariate(0, 1)}')

my_list = list('abcd')
print(f'The list: {my_list}')
print(f'Random item from the list: {random.choice(my_list)}')
print(f'3 Random unique items from the list: {random.sample(my_list, 3)}')
print(f'3 items from the list, repeats ok: {random.choices(my_list, k=3)}')
random.shuffle(my_list)
print(f'Shuffle the list: {my_list}')

# re-use randomly generated numbers using seeds
# note: not good for security
print('\nCreate seeds for random number generation:')
random.seed(1)
a = random.random()
b = random.randint(1, 10)
print(f'seed 1: {a} {b}')
random.seed(2)
c = random.random()
d = random.randint(1, 10)
print(f'seed 2: {c} {d}')

print('\nRe-create those same random numbers using seeds.')
random.seed(1)
a = random.random()
b = random.randint(1, 10)
print(f'seed 1: {a} {b}')
random.seed(2)
c = random.random()
d = random.randint(1, 10)
print(f'seed 2: {c} {d}')

# for number gener
# ation involving security, use the 'secrets' module
e = secrets.randbelow(10)  # 0 up to but not including 10.
print(f'\nA truly random integer up to, but not including 10: {e}')
f = secrets.randbits(4)  # a random 4-bit number.
print(f'A truly random 4-bit number: {f}')
g = secrets.choice(my_list)
print(f'A truly random choice from the list {my_list}: {g}')
