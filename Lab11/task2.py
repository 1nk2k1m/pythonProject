import os

directory = "./"
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
print("Files in directory:", files)
