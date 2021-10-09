class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
            self.c = c
            

    def is_triangle(self):
        if self.a + self.b>self.c and self.c+self.b>self.a and self.a+self.c>self.b:
            print('Ура, можно построить треугольник!')
        elif self.a < 0 or self.b < 0  or self.c < 0:
            print('С отрицательными числами не выйдет')
        else:
            print('Жаль, но из этого не сделать треугольник.')

t = TriangleChecker(int(input()), int(input()), int(input()))
t.is_triangle()
