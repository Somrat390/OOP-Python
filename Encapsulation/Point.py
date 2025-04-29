class Point:
    def __init__(self,x, y):
        self.x_cod = x
        self.y_code = y
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_code)
    def euclidiandistance(self):

p1 = Point(0,0)
print(p1)
p2 = Point(-2,2)
print(p2)