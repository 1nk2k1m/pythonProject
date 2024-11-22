list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]

result = [item for item in list1 if item not in list2]
print(result)
