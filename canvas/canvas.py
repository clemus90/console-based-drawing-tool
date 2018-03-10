from collections import deque

class Canvas:
    """Simple console based canvas"""
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("dimensions cannot be negative: w: {0} h: {1}".format(width, height))
        self._height = height
        self._width = width if height > 0 else 0
        # defined matrix with added padding for the borders of the canvas
        self._matrix = [self.generate_horizontal_frame()]
        for i in range(self._height):
            self.matrix.append(self.generate_inner_row())
        self.matrix.append(self.generate_horizontal_frame())

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        """Set the inner matrix to a different layout, assumes the user will respect the format
        that is returned when a string representation is asked, dash '-' for frame, 'x' for lines
        and any other character for filling"""
        new_height = len(matrix) - 2
        new_width = len(matrix[0]) - 2
        if new_height < 0 or new_width < 0:
            raise ValueError("invalid matrix: {0}".format(matrix))
        self._matrix = matrix
        self._height = new_height
        self._width = new_width

    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width

    def in_range(self, x, y):
        """checks if a given coordinate x-y is inside the canvas"""
        return 0 < x <= self.width and  0 < y <= self.height

    def in_range_point(self, point):
        """checks if the given point (x,y) is inside the canvas"""
        (x, y) = point
        return self.in_range(x, y)

    def generate_horizontal_frame(self):
        """ given the width property of a canvas, returns the horizontal frames for
        the upper and lower parts"""
        return ['-' for i in range(self.width + 2)]
    
    def generate_inner_row(self):
        """ makes the inner content of the canvas empty with the frame characters at
        each side"""
        return ['|'] + [' ' for x in range(self.width)] + ['|']

    def __str__(self):
        return '\n'.join([''.join(self.matrix[i]) for i in range(self.height + 2)])

    def draw_line(self, x1, y1, x2, y2):
        """ given two points in the space draws a line from p1 to p2, it can only draw
        vertical and horizontal lines"""
        if x1 == x2:
            self.draw_vertical_line(x1, y1, y2)
        elif y1 == y2:
            self.draw_horizontal_line(y1, x1, x2)
        else:
            print("Only Vertical and Horizontal lines supported")
    
    def draw_vertical_line(self, x, y1, y2):
        """ given the x position draws a line of length |y2 - y1|"""
        (origin, end) = (min(y1, y2), max(y1, y2))
        if not (self.in_range(x, y1) and 
            self.in_range(x, y2)):
                print("Line out of range")
        else:
            for i in range(origin, end + 1):
                self.matrix[i][x] = "x"
    
    def draw_horizontal_line(self, y, x1, x2):
        """ given the y position draws a line of length |x2 - x1|"""
        (origin, end) = (min(x1, x2), max(x1, x2))
        if not (self.in_range(x1, y) 
            and self.in_range(x2, y)):
                print("Line out of range")
        else:
            for i in range(origin, end + 1):
                self.matrix[y][i] = "x"
    
    def draw_rectangle(self, x1, y1, x2, y2):
        """ given two points in the space draws a rectangle parallel to the x and y
        axis with using the points as upper left corner and lower right corner"""
        (min_x, max_x, min_y, max_y) = (min(x1, x2), max(x1, x2),
            min(y1, y2), max(y1, y2))
        if not (self.in_range(min_x, min_y) 
            and self.in_range(max_x, max_y)):
                print("Rectangle out of range")
        else:
            self.draw_horizontal_line(min_y, min_x, max_x)
            self.draw_horizontal_line(max_y, min_x, max_x)
            self.draw_vertical_line(min_x, min_y, max_y)
            self.draw_vertical_line(max_x, min_y, max_y)

    def fill(self, x, y, colour):
        """ given a point in space and a colour, fill the space spreading from the point
        vertically and horizontally stoping at borders (x) and frames (| or -)"""
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
                    advance_y = (x0, y0 + e)
                    advance_x = (x0 + e, y0)
                    for point in [advance_x, advance_y]:
                        if (self.in_range_point(point) and (point not in visited) and
                            self.matrix[point[1]][point[0]] != "x"):
                                queue.append(point)
    
    @staticmethod
    def from_layout(layout):
        """returns a canvas from a matrix layout"""
        matrix = [[item for item in line] for line in layout.split("\n")]
        new_canvas = Canvas(0, 0)
        new_canvas.matrix = matrix
        return new_canvas

