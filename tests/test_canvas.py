from .context import canvas
import pytest

Canvas = canvas.Canvas

@pytest.fixture
def init_1():
    return '\n'.join(["-----",
                      "|   |",
                      "|   |",
                      "|   |",
                      "-----",])

@pytest.fixture
def init_2():
    return '\n'.join(["------",
                      "|    |",
                      "|    |",
                      "|    |",
                      "|    |",
                      "------",])

@pytest.fixture
def lines_1():
    return '\n'.join(["-----",
                      "| x |",
                      "| xx|",
                      "|   |",
                      "-----",])

@pytest.fixture
def lines_2():
    return '\n'.join(["------",
                      "|   x|",
                      "|   x|",
                      "|   x|",
                      "|xxx |",
                      "------",])

@pytest.fixture
def rectangle_1():
    return '\n'.join(["-----",
                      "|xx |",
                      "|xx |",
                      "|   |",
                      "-----",])

@pytest.fixture
def rectangle_2():
    return '\n'.join(["------",
                      "| xxx|",
                      "| x x|",
                      "| xxx|",
                      "|    |",
                      "------",])

@pytest.fixture
def fill_1():
    return '\n'.join(["-----",
                      "| xc|",
                      "| xx|",
                      "|   |",
                      "-----",])

@pytest.fixture
def fill_2():
    return '\n'.join(["------",
                      "|cxxx|",
                      "|cx x|",
                      "|cxxx|",
                      "|cccc|",
                      "------",])
    
def test_constructor_3x3(init_1):
    assert str(Canvas(3, 3)) == init_1

def test_constructor_4x4(init_2):
    assert str(Canvas(4,4)) == init_2

def test_constructor_negative_dimensions():
    with pytest.raises(ValueError):
        Canvas(-1, -1)

def test_matrix_property(init_1, init_2):
    assert Canvas(3,3).matrix == [[i for i in line] for line in init_1.split("\n")]
    assert Canvas(4,4).matrix == [[i for i in line] for line in init_2.split("\n")]

def test_matrix_setter(init_1):
    c = Canvas(0,0)
    c.matrix = [[i for i in line] for line in init_1.split("\n")]
    assert str(c) == init_1

def test_matrix_dimensions():
    for i in range(1,5):
        for j in range(1,5):
            c = Canvas(i,j)
            assert c.height == j
            assert c.width == i

def test_0_height_dimension():
    for i in range(1, 5):
        c = Canvas(i, 0)
        assert c.width == 0

def test_in_range():
    c = Canvas(5, 5)
    for i in range(1, 5):
        for j in range(1,5):
            assert c.in_range(i,j)
    for i in range(1, 5):
        assert not c.in_range(0,i)
        assert not c.in_range(0,j)
        assert not c.in_range(6,i)
        assert not c.in_range(6,j)

def test_in_range_point():
    c = Canvas(5, 5)
    for i in range(1, 5):
        for j in range(1,5):
            assert c.in_range_point((i,j))
    for i in range(1, 5):
        assert not c.in_range_point((0,i))
        assert not c.in_range_point((0,j))
        assert not c.in_range_point((6,i))
        assert not c.in_range_point((6,j))

def test_horizontal_frame(init_1, init_2):
    c = Canvas(3,3)
    assert c.generate_horizontal_frame() == [x for x in init_1.split('\n')[0]]
    c = Canvas(4,4)
    assert c.generate_horizontal_frame() == [x for x in init_2.split('\n')[0]]

def test_inner_row(init_1, init_2):
    c = Canvas(3,3)
    assert c.generate_inner_row() == [x for x in init_1.split('\n')[1]]
    c = Canvas(4,4)
    assert c.generate_inner_row() == [x for x in init_2.split('\n')[2]]

def test_draw_lines_3x3(init_1, lines_1):
    origin_1 = Canvas.from_layout(init_1)
    #should be ignored
    origin_1.draw_line(2, 1, 2, 4)
    assert str(origin_1) == init_1
    origin_1.draw_line(2, 1, 2, 2)
    origin_1.draw_line(2, 2, 3, 2)
    assert str(origin_1) == lines_1

def test_draw_lines_4x4(init_2, lines_2):
    origin = Canvas.from_layout(init_2)
    #should be ignored
    origin.draw_line(2, 2, 2, 6)
    assert str(origin) == init_2
    origin.draw_line(4, 1, 4, 3)
    origin.draw_line(3, 4, 1, 4)
    assert str(origin) == lines_2

def test_draw_rectangles_3x3(init_1, rectangle_1):
    origin = Canvas.from_layout(init_1)
    #should be ignored
    origin.draw_rectangle(2, 1, 2, 4)
    assert str(origin) == init_1
    origin.draw_rectangle(1, 1, 2, 2)
    assert str(origin) == rectangle_1

def test_draw_rectangles_4x4(init_2, rectangle_2):
    origin = Canvas.from_layout(init_2)
    #should be ignored
    origin.draw_line(2, 2, 2, 6)
    assert str(origin) == init_2
    origin.draw_rectangle(4, 3, 2, 1)
    assert str(origin) == rectangle_2

def test_draw_fill_3x3(lines_1, fill_1):
    origin = Canvas.from_layout(lines_1)
    origin.fill(3, 1, "c")
    assert str(origin) == fill_1

def test_draw_fill_4x4(rectangle_2, fill_2):
    origin = Canvas.from_layout(rectangle_2)
    origin.fill(1, 1, "c")
    assert str(origin) == fill_2