class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = int(diameter)
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.radius

    def calculate_area(self):
        return Circle.__pi * (self.radius**2)

    def calculate_area_of_sector(self, angle):
        __area_sector = (self.calculate_area() / 360) * angle
        # __area_sector = self.calculate_area() * (angle/360)
        # __area_sector = self.calculate_area() / (360/angle)
        return __area_sector


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")


