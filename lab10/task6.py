def calculate_expression(n):
    n_str = str(n)
    return int(n_str) + int(n_str * 2) + int(n_str * 3)


n = int(input("Enter an integer: "))
print("Result:", calculate_expression(n))
