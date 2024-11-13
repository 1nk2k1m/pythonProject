def first_and_last(items):
    if items:
        print("First item:", items[0])
        print("Last item:", items[-1])
    else:
        print("List is empty")


items = input("Enter items separated by a comma: ").split(",")
first_and_last(items)
