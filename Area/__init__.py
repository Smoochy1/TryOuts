from Polygon import Rectangle, Square, Triangle, Circle

def area(a):
    if isinstance(a, Rectangle):
        return f"The Area of given Rectangle is {a.l * a.b}"
    elif isinstance(a, Square):
        return f"The Area of given Square is {a.a ** 2}"
    elif isinstance(a, Triangle):
        s = (a.a1 + a.a2 + a.a3) / 2
        return f"The Area of given Triangle is {((s * (s - a.a1) * (s - a.a2) * (s - a.a3)) ** 0.5):.2f}"
    elif isinstance(a, Circle):
        return f"The Area of given Circle is {3.14 * (a.r ** 2):.2f}"
