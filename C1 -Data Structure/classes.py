from page9classes import Area, _Circle

if __name__ == "__main__":
    rect1 = Area(5,6)
    rect1.area_cal()
    print(rect1.area)

    circle1 = _Circle(5)
    circle1._calarea()
    print(circle1._area)

