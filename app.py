from pathlib import Path

path = Path("python")
for file in path.glob('*'): # find all files in a directory
    print(file)

# print(path.mkdir()) # create a directory
# path.rmdir()  # remove a directory