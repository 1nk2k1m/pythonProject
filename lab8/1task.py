print("task 1.1")
user_input = input("Enter a string: ").lower()
char_list = list(user_input)
print("Created list is:", char_list)
print()


print("task 1.2")
input_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]
list_vow, list_cons, list_sym = [], [], []
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
for item in input_list:
    char, count = item
    if char in vowels:
        list_vow.append(item)
    elif char in consonants:
        list_cons.append(item)
    else:
        list_sym.append(item)

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)
