import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

    def __ge__(self,other):
        return self.x >= other.x and self.y >= other.y
    
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y

    def __le__(self,other):
        return self.x <= other.x and self.y <= other.y

    def __lt__(self,other):
        return self.x < other.x and self.y < other.y

    def distance(self,other):
        x_portion = (other.x-self.x)**2
        y_portion = (other.y-self.y)**2
        return math.sqrt( x_portion + y_portion )
    


if __name__ == '__main__':
    p1 = Point(2,2)
    print(p1)
    p2 = Point(1,1)
    print(p2)
    if p1 > p2:
        if (p1 == p2):
            print("p1 == p2")
        else:
            print("p1 > p2")
    else:
        print("p1 != p2")