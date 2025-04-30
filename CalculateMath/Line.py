class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return f"{self.A}x {'+' if self.B >= 0 else "-"} {abs(self.B)}y {'+' if self.C >= 0 else "-"} {abs(self.C)}"

    def lineonPoint(self,point):
        if self.A*point.x_cod +self.B*point.y_code + self.C == 0:
            return "lies on the lien"
        else:
            return "Doesnt lie on the line"