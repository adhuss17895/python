try:
    age = int(input("Enter the age:"))
    print(age)
except ValueError:
    print("Invalid input!! Please try again")