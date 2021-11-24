class Radius():
    def __init__(self,radius):
        self.radius=radius
    def printval(self):
        print("radius is",self.radius)

class Circle(Radius):
    def __init__(self,radius):
        super().__init__(radius)

    def print(self):
       print("area is=",(22/7)*self.radius*self.radius)


p=Circle(7)
p.print()