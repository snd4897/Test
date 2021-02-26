class Cylinder:
    pi = 3.14

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius * self.radius * self.height

    def surface_area(self):
        return 2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius ** 2


Cy = Cylinder(30, 5)

print(f'volume of the cylinder is {Cy.volume()}')

print(f'surface area of the cylinder is {Cy.surface_area()}')
