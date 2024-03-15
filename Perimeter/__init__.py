from Polygon import Rectangle, Square, Triangle, Circle
def peri(a): 
    if isinstance(a,Rectangle):
        return f"The Perimeter of given Rectangle is {2*(a.l+a.b)}"
    elif isinstance(a,Square):
        return f"The Perimeter of givne Square is {4*a.a}"
    elif isinstance(a,Triangle):
        return f"The Perimeter of given Triangle is {a.a1+a.a2+a.a3}"
    elif isinstance(a,Circle):
        return f"The Perimeter of given Circle is {3.14*2*a.r:.2f}"