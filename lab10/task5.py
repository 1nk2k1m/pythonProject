def get_file_extension(filename):
    try:
        extension = filename.split(".")[-1]
        if extension == filename:
            raise ValueError("No extension found")
        return extension
    except ValueError as e:
        print(e)


filename = input("Enter a file name: ")
print("File extension:", get_file_extension(filename))
