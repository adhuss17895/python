weight = int(input('Enter the weight: '))
type = input('(L)bs or (K)g: ' )

if (type=='L') or (type=='l'):
    print("Weight in (K)gs is: ", 0.45 * weight)
elif (type=='K') or (type=='k'):
    print("Weight inb (L)bs is: ", 2.2 * weight)
else:
    print("Wrong input option")

