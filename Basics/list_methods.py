#REMOVING DUPLICATES FROM A LIST
numbers = [2, 5, 8, 11, 2, 6, 7, 1, 6]
unix = []
for number in numbers:
    if number not in unix:
        unix.append(number)

print(unix)