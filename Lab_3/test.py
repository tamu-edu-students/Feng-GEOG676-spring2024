class Shape():
    def __init__(self):
        pass

class cir(Shape):
    def __init__(self, r):
        self.r = r
        self.area = r **2
    def print_area(self):
        print('The area is: ', self.area)


cir(5).print_area()
