class Point:
    def __init__(self,x,y):  #constructor
        self.x = x
        self.y = y
    def draw(self):
        print("Draw")
    def move(self):
        print("move")

point1 = Point(20,40) #Object of class Point
a = int(input('Enter value of a:'))
b = int(input('Enter value of b:'))
point2 = Point(a,b)

#Attribues of object

point1.draw() 

print(f'{point1.x} , {point1.y}')

point2.draw() 

print(f'{point2.x} , {point2.y}')
