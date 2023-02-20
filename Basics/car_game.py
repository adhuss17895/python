command = ""
started = False

while True:
    command = input('>')
    if command.lower() == 'start':
        if started:
            print("Car has already been started...")
        else:
            started = True
            print(" Car has abeen started...")
    elif command.lower() == 'stop':
        if started:
            started = False
            print("Car has been stopped...")
        else:
            
            print("Car has already been stopped...")
    elif command.lower() == 'help':
        print(''' 
start - to start the car
stop - to stop the car
quit - exit application''')
    elif command.lower() == 'quit':
        print("App exit...")
        break
    else:
        print("Wrong input command")
    

    