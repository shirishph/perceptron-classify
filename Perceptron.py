import plotille


class Perceptron(object):
    def __init__(self):
        print("__init__")

    def train(self):
        print("train")

        data_points = [
            [8, 28, "SW"],
            [8, 1, "SW"],
            [30, 17, "SW"],
            [14, 13, "SW"],
            [11, 4, "SW"],
            [32, 34, "SW"],
            [9, 33, "SW"],
            [17, 2, "SW"],
            [34, 7, "SW"],
            [19, 28, "SW"],
            [29, 24, "SW"],
            [10, 34, "SW"],
            [5, 1, "SW"],
            [5, 25, "SW"],
            [5, 8, "SW"],
            [28, 24, "SW"],
            [16, 34, "SW"],
            [22, 1, "SW"],
            [21, 34, "SW"],
            [27, 2, "SW"],
            [21, 13, "SW"],
            [7, 33, "SW"],
            [35, 18, "SW"],
            [10, 27, "SW"],
            [1, 9, "SW"],
            [84, 99, "NE"],
            [97, 80, "NE"],
            [90, 89, "NE"],
            [96, 95, "NE"],
            [86, 83, "NE"],
            [86, 68, "NE"],
            [80, 91, "NE"],
            [71, 98, "NE"],
            [99, 75, "NE"],
            [66, 87, "NE"],
            [97, 66, "NE"],
            [88, 78, "NE"],
            [71, 92, "NE"],
            [94, 74, "NE"],
            [96, 77, "NE"],
            [84, 71, "NE"],
            [75, 94, "NE"],
            [90, 85, "NE"],
            [69, 81, "NE"],
            [98, 94, "NE"],
            [75, 96, "NE"],
            [70, 68, "NE"],
            [94, 87, "NE"],
            [84, 92, "NE"],
            [93, 85, "NE"]
        ]

        c = plotille.Canvas(width=40, height=20)
        c.rect(0.0, 0.0, 0.99, 0.99)
        for element in data_points:
            c.point(element[0] / 100.0, element[1] / 100.0)
        print(c.plot())

        return True
