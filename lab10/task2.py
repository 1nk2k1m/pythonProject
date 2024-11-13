def convert_seconds(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"


seconds = int(input("Enter the number of seconds: "))
print("Converted time:", convert_seconds(seconds))
