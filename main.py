from Canvas import Canvas
from functools import wraps

def identity(x):
    return x

def validate_command_args(message, transformations):
    def decorator(f):
        @wraps(f)
        def wrapper(*args):
            if len(args) != len(transformations):
                print(message)
            else:
                return f(*[transformations[i](args[i]) for i in range(len(args))])
        return wrapper
    return decorator

@validate_command_args("New canvas usage example: C 10 9", [identity, int, int])
def create_canvas(canvas, w, h):
    return (False, Canvas(w,h))

@validate_command_args("Draw Line usage example: L 1 2 6 2",
    [identity, int, int, int, int])
def draw_line(canvas, x0, y0, x1, y1):
    canvas.draw_line(x0, y0, x1, y1)

@validate_command_args("Draw Rectangle usage example: R 1 2 6 2",
    [identity, int, int, int, int])
def draw_rectangle(canvas, x0, y0, x1, y1):
    canvas.draw_rectangle(x0, y0, x1, y1)

@validate_command_args("Fill usage example: B 10 3 s", 
    [identity, int, int, identity])
def fill(canvas, x0, y0, colour):
    canvas.fill(x0, y0, colour)

@validate_command_args("Quit syntax: Q", [identity])
def quit_app(canvas):
    return (True, canvas)

def not_supported(*args):
    print("Command not supported")


def command_selector(canvas, command):
    args = command.split(' ')
    operation = args[0]
    subArgs = args[1:]
    if operation != "C" and operation != "Q" and canvas is None:
        print("A canvas needs to be initializated first using the command 'C'")
    else:
        commands = {
            "C": create_canvas,
            "L": draw_line,
            "R": draw_rectangle,
            "B": fill,
            "Q": quit_app
        }
        f = commands.get(operation, not_supported)
        ret = f(*([canvas] + subArgs))
        if ret is not None:
            return ret
    return (False, canvas)

def main():
    loop_break = False
    current_canvas = None

    while not loop_break:
        command = input("enter command: ")
        (loop_break, current_canvas) = command_selector(current_canvas, command)
        if current_canvas is not None:
            print(current_canvas)

if __name__ == "__main__":
    main()