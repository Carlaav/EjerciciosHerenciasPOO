class Punto2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def translacion(self,a,b):
        self.x=self.x+a
        self.y=self.y+b
class Punto3D:
    def __init__(self,x,y,z):
        self.punto2d=Punto2D(x,y)
        self.z=z
    def translacion(self,a,b,c):
        self.punto2d.x=self.punto2d.x+a
        self.punto2d.y=self.punto2d.y+b
        self.z=self.z+c
        print("x:",self.punto2d.x, "y:",self.punto2d.y,"z:",self.z)