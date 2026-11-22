class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + " , " + str(self.y) + ") "

class Rectangle:

    def __init__(self, p, q):
        self.p = p
        self.q = q
        assert isinstance(p, Point) and isinstance(q, Point) and p.x <= q.x and p.y <= q.y, "Bad input!"

    def __str__(self):
        return "(p=(" + str(self.p.x) + ", " + str(self.p.y) + "), q=(" + str(self.q.x) + ", " + str(self.q.y) + "))"

    def get_width(self):
        return self.q.x - self.p.x

    def get_height(self):
        return self.q.y - self.p.y

    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())

    def area(self):
        return self.get_width() * self.get_height()

    def contains(self, pt):
        assert isinstance(pt, Point), "Bad Input!"

        return (self.p.x <= pt.x <= self.q.x and
                self.p.y <= pt.y <= self.q.y)
p1= Point(1,2)
p2= Point(3.2,4)
R= Rectangle(p1,p2)
print(R)
print(R.get_width())
print(R.get_height())
print(R.area())
print(R.perimeter())
print(R.contains(Point(1.5,3)))
print(R.contains(Point(10.5,3)))
print(R.contains(Point(1,2)))
print(R.contains(Point(3.2,4)))