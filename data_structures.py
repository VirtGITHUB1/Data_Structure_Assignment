my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

removed = my_list.pop()   # same as my_list.pop(-1)
print("removed:", removed)

my_list.sort()
print("Final list:", my_list)

print("Index of 30:", my_list.index(30))

# Outputs
# removed: 70
# Final list: [10, 15, 20, 30, 40, 50, 60]
# Index of 30: 3
