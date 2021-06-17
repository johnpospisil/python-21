fruits = ["banana", "apple", "cherry"]
print("The first fruit in the list is " + fruits[0])
print("The first two fruits in the list:")
print(fruits[0:2])
print("The last two fruits in the list: ")
print(fruits[1:3])
print("")

for fruit in fruits:
    print(fruit)

if "cherry" in fruits:
    print("You have cherries!")
else:
    print("You don't have cherries.")

print("You have " + str(len(fruits)) + " fruits.")

# List Functions
# fruits2 = ["lemon", "papaya"]
fruits.append("mango")
fruits.extend(["lemon", "papaya", "apple", "dragon fruit"])
print("Appended fruit list:")
print(fruits)

fruits.insert(1, "blueberry")
print("Insert blueberry to the fruit list:")
print(fruits)

print("How may times does \"apple\" apprear in the list?")
print(fruits.count("apple"))

fruits.pop()
print("Pop the last item from the fruit list:")
print(fruits)

# a few ways to remeve an element - .remove() and del()
fruits.remove("cherry")
print("Remove 'cherry' from the fruit list:")
print(fruits)

del(fruits[-1])
print("Delete the last element from the fruit list:")

fruits.reverse()
print("Reversed the fruit list:")
print(fruits)

# sort two different ways

print(sorted(fruits))  # returns a sorted list

fruits.sort()  # sorts the source list
print("Sort the fruit list:")
print(fruits)

# make complete copies of a list - 3 ways to do it
fruits3 = fruits.copy()
fruits4 = list(fruits)
fruits5 = fruits[:]
print("Three complete copies of the fruit list:")
print(fruits3)
print(fruits4)
print(fruits5)


print("The index for \"lemon\" in the fruit list is: ")
print(fruits.index("lemon"))

print("The first fruit is: ")
print(fruits[0])

fruits.clear()
print(f"Clear the fruit list: {fruits}\n")

# create a manipulated list in one line with this format
num_list = [1, 2, 3, 4, 5, 6, 7]
squared_num_list = [num*num for num in num_list]
print(f'Original list: {num_list}\nManipulated List: {squared_num_list}')

# 2-Dimensional Lists i.e. a list of lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]

print(number_grid[0][0])
print(number_grid[1][2])
print(number_grid[3][0])

number_grid[3][0] = 10
print(number_grid[3][0])
