def midpoint(x1, y1, x2, y2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)


def main():
    x1, y1, x2, y2 = 1, 2, 3, 4
    mid_point1 = midpoint(x1, y1, x2, y2)
    print("Midpoint:", mid_point1)

    x1, y1, x2, y2 = -1, 3, 6, 7
    mid_point2 = midpoint(x1, y1, x2, y2)
    print("Midpoint:", mid_point2)

if __name__ == "__main__":
    main()
