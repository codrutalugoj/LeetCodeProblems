class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def equals(self, p2):
        return self.x == p2.x and self.y == p2.y
    
def collinear(p1: Point, p2: Point, p3: Point):

    if p1.equals(p2) or p1.equals(p3) or p2.equals(p3):
        return True
    
    if p1.x == p2.x:
        return p3.x == p1.x

    b = (p2.y - p1.y)/(p2.x - p1.x)

    a = p2.y - b * p2.x

    return abs(p3.y - (a + b * p3.x)) <= 0.00001

if __name__ == "__main__":
    print(collinear(Point(1, 1), Point(2, 2), Point(3, 3)))
    print(collinear(Point(1, 1), Point(2, 2), Point(3, 2)))
    print(collinear(Point(1, 1), Point(1, 1), Point(2, 2)))
    print(collinear(Point(1, 0), Point(1, 1), Point(2, 2)))
    print(collinear(Point(2, 2), Point(1, 1), Point(1, 0)))
    print(collinear(Point(3, 3), Point(6, 6), Point(9, 9)))