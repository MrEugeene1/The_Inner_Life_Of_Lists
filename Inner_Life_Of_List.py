# Abnormalities of list
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# Solution to the abnormalities is by slicing
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# General forms of slicing
# my_list(start:end) where end = end -1
# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
