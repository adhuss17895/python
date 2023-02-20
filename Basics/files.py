try:
        fhand = open('/home/adhuss/Desktop/Adhi_Work/Repo/python/Basics/example.txt')
        count = 0

        for line in fhand:
            count = count + 1
            
        print(f'No of lines is {count} !!')
except FileNotFoundError:
    print("File not found!!")