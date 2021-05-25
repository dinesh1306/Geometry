class Geometry:
    pi = 3.14


class Square(Geometry):
    def cal_perimeter(self, length):
        return 4*length

    def cal_area(self, length):
        return length*length


class Rectangle(Geometry):
    def cal_perimeter(self, width, length):
        return 2*width + 2*length

    def cal_area(self, width, length):
        return length * width


class Triangle(Geometry):
    def cal_perimeter(self, len1, len2, len3):
        return len1 + len2 + len3

    def cal_area(self, base, height):
        return (1 / 2) * base * height


class Circle(Geometry):
    def cal_diameter(self, radius):
        return 2*radius

    def cal_circumference(self, radius):
        return 2*Geometry.pi*radius

    def cal_area(self,radius):
        return Geometry.pi*radius*radius
