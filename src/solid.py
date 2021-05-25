class Solid:
    pi = 3.14


class Sphere(Solid):
    def cal_surface_area(self, radius):
        return 4*Solid.pi*radius*radius

    def cal_volume(self, radius):
        return (4/3)*Solid.pi*radius*radius*radius

    def cal_diameter(self, radius):
        return 2*radius


class Cone(Solid):
    def cal_base_area(self, radius):
        return Solid.pi*radius*radius

    def cal_volume(self, height, radius):
        return (1/3)*Solid.pi*radius*radius*height


class Cube(Solid):
    def cal_area(self, side):
        return 6*side*side

    def cal_volume(self, side):
        return side*side*side
