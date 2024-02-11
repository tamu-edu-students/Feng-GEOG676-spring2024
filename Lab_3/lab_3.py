import math

try: #input text
    imput_text = open(r'Feng-GEOG676-spring2024/Lab_3/shape.txt', 'r')
    text_lines = imput_text.readlines()
    imput_text.close()
except IOError:
    print("An error has occurred")

#creat class
class Shape():  # creat general shape class
    def __init__(self):
        pass

class Rectangle(Shape):  # creat rectangle shape class
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)
        self.area = self.length * self.width
    def printArea(self): #print the area
        print("Area of the rectangle is: ", self.area)
    
class Circle(Shape):  # creat circle shape class
    def __init__(self, radius):
        self.radius = int(radius)
        self.area = math.pi * self.radius ** 2
    def printArea(self): #print the area
        print("Area of the circle is: ", self.area)
    
class Triangle(Shape):   # creat triangle shape class
    def __init__(self, bottom, height):
        self.bottom = int(bottom)
        self.height = int(height)
        self.area = self.bottom * self.height / 2
    def printArea(self): #print the area
        print("Area of the triangle is: ", self.area)

def creat_shape(imputs):    #function of creat shape from imput text
    for imput in imputs:
        raw_shape = imput.split(',')
        shape_name = raw_shape[0]

        if shape_name == 'Rectangle':   #creat rectangle and print the area
            shape_rect = Rectangle(raw_shape[1], raw_shape[2])
            shape_rect.printArea()

        elif shape_name == 'Circle':   #creat circle and print the area
            shape_cir = Circle(raw_shape[1])
            shape_cir.printArea()

        elif shape_name == 'Triangle':  #creat triangle and print the area
            shape_tri = Triangle(raw_shape[1], raw_shape[2])
            shape_tri.printArea()
        
        else: pass

creat_shape(text_lines)     #creat shpes by the data from the imported text