def even_numbers_until_237(numbers):
    for num in numbers:
        if num == 237:
            break
        if num % 2 == 0:
            print(num)


numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
even_numbers_until_237(numbers)
