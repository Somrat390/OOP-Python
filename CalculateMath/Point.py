from Line import Line

class Point:
    def __init__(self,x, y):
        self.x_cod = x
        self.y_code = y
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_code)
    def euclidiandistance(self,other):
        return ((self.x_cod - other.x_cod) ** 2 + (self.y_code - other.y_code) ** 2)**0.5
    def distance_from_origin(self):
        return self.euclidiandistance(Point(0,0))
    def shortestdistance(point,line):
        return abs(line.A*point.x_cod + line.B*point.y_code + line.C)/(line.A**2 + line.B ** 2)**0.5

p1 = Point(0,0)
print(p1)
p2 = Point(1,10)
print(p2)

print(p1.euclidiandistance(p2))
print(p1.distance_from_origin())

p3 = Line(1,1,-2)
print(p3)
print(p3.lineonPoint(p1))

print(p2.shortestdistance(p3))