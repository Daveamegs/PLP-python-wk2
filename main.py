# Create an empty list
my_list = list()

# Append elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert value at the second position
my_list[1] = 15

# Extend my_list with another list
my_list.extend([50, 60, 70])

# Remove last element
my_list.pop()

# Sort list in ascending order
my_list.sort()

# Find and print the index of the value 30
for i in range(0, len(my_list)):
    if my_list[i] == 30:
        print(i)
