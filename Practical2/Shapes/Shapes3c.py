import math


class Point:
    def __init__(self, X, Y):
        self._x = X
        self._y = Y
        self._coords = [X, Y]
    def get_xcoord(self):
        return self._x
    def get_ycoord(self):
        return self._y
    def distance_from_origin(self):
        return math.sqrt(self._y**2 + self._x**2)
    def __str__(self):
        return "Point (" + str(self.get_xcoord()) + ", " + str(self.get_ycoord()) + ") is that far from the origin: " + str(self.distance_from_origin())








class Shape():
   def __init__(self,  colour, X, Y):

       self._centre = Point(X,Y)
       self._colour = colour
   def get_colour(self):
       return self._colour

class Circle(Shape):
    def __init__(self, colour, radius, X, Y):
        super().__init__(colour, X, Y)
        self._radius = radius
    def get_area(self):
        return math.pi*self._radius*self._radius
    def get_radius(self):
        return self._radius
    def __str__(self):
        return "Circle of radius " + str(self.get_radius()) + " and colour " + str(self.get_colour())





class Cylinder(Shape):
    def __init__(self, colour, radius, height, X, Y):
        super().__init__(colour, X, Y)
        self._base = Circle(colour, radius, X, Y)
        self._height = height
    def get_area(self):
        return 2*math.pi*self.get_radius()*self._height + 2*math.pi*self.get_radius()**2
    def get_volume(self):
        return math.pi*self.get_radius()**2*self._height
    def __str__(self):
       return "Cylinder of radius " + str(self._.get_radius()) + ", colour " + self.get_colour() +", volume " + str(self.get_volume())
        
#cylinder = Cylinder ("red", 7.16, 3.61)     
#print (cylinder)

class Rectangle(Shape):
    def __init__(self, colour, width, length, X, Y):
        super().__init__( colour, X, Y)
        self._width = width
        self._length = length
    def get_area(self):
        return self._width*self._length
    def get_perimeter(self):
        return 2*self._width+2*self._length
    def __str__(self):
        return "rectangle of width " + str(self._width) + " length " + str(self._length) + " colour " + str(self.get_colour())


def test_shapes():
        
        rectangle = Rectangle("red", 3, 4, 5, 6)
        cylinder = Cylinder("green", 3, 5, 8, 9)
        
        #print(rectangle._centre.distance_from_origin())

        #print(circle)
        print(rectangle)
        print(cylinder)
        


test_shapes()