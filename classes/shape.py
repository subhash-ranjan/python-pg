class Polygon:
    def __init__(self, sides, name, size=100,color='black', line_thickness=3):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides
        self.line_thickness = line_thickness

    # def draw(self):
    #     turtle.color(self.color)
    #     turtle.pensize(self.line_thickness)
    #     for i in range(self.sides):
    #         turtle.forward(self.size)
    #         turtle.right(180-self.angle)
   
   
    # square =  Polygon(4, 'square',size=100, color="black", line_thickness=3)
       
