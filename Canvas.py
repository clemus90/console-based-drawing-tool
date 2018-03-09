from collections import deque

class Canvas:
    """Simple console based canvas"""
    def __init__(self, width, height):
        self.height = height
        self.width = width
        # defined matrix with added padding for the borders of the canvas
        self.matrix = [self.generate_horizontal_border()]
        for i in range(self.height):
            self.matrix.append(self.generate_inner_row())
        self.matrix.append(self.generate_horizontal_border())

    def in_range(self, x, y):
        return x > 0 and x <= self.width and y > 0 and y <= self.height

    def in_range_point(self, point):
        (x, y) = point
        return self.in_range(x, y)

    def generate_horizontal_border(self):
        return ['-' for i in range(self.width + 2)]
    
    def generate_inner_row(self):
        return ['|'] + [' ' for x in range(self.width)] + ['|']

    def print(self):
        for i in range(self.height + 2):
            print(''.join(self.matrix[i]))

    def draw_line(self, x1, y1, x2, y2):
        if x1 == x2:
            self.draw_vertical_line(x1, y1, y2)
        elif y1 == y2:
            self.draw_horizontal_line(y1, x1, x2)
        else:
            print("Only Vertical and Horizontal lines supported")
    
    def draw_vertical_line(self, x, y1, y2):
        (origin, end) = (min(y1, y2), max(y1, y2))
        if not (self.in_range(x, y1) and 
            self.in_range(x, y2)):
                print("Line out of range")
        else:
            for i in range(origin, end + 1):
                self.matrix[i][x] = "x"
    
    def draw_horizontal_line(self, y, x1, x2):
        (origin, end) = (min(x1, x2), max(x1, x2))
        if not (self.in_range(x1, y) 
            and self.in_range(x2, y)):
                print("Line out of range")
        else:
            for i in range(origin, end + 1):
                self.matrix[y][i] = "x"
    
    def draw_rectangle(self, x1, y1, x2, y2):
        (minX, maxX, minY, maxY) = (min(x1, x2), max(x1, x2),
            min(y1, y2), max(y1, y2))
        if not (self.in_range(minX, minY) 
            and self.in_range(maxX, maxY)):
                print("Rectangle out of range")
        else:
            self.draw_horizontal_line(minY, minX, maxX)
            self.draw_horizontal_line(maxY, minX, maxX)
            self.draw_vertical_line(minX, minY, maxY)
            self.draw_vertical_line(maxX, minY, maxY)

    def fill(self, x, y, colour):
        if not self.in_range(x, y):
            print("Fill origin out of range")
        else:
            visited = set()
            queue = deque([(x,y)])
            while queue:
                (x0, y0) = queue.popleft()
                visited.add((x0,y0))
                self.matrix[y0][x0] = colour
                for e in [-1, 1]:
                    advanceY = (x0, y0 + e)
                    advanceX = (x0 + e, y0)
                    for point in [advanceX, advanceY]:
                        if (self.in_range_point(point) and (point not in visited) and
                            self.matrix[point[1]][point[0]] != "x"):
                                queue.append(point)
