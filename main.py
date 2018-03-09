from Canvas import Canvas

def command_selector(canvas, command):
    args = command.split(' ')
    operation = args[0]
    subArgs = args[1:]
    if operation != "C" and canvas is None:
        print("A canvas needs to be initializated first using the command 'C'")
    elif operation == "C":
        if len(subArgs) != 2:
            print("New canvas usage example: C 10 9")
        else:
            return (False, Canvas(*[int(x) for x in subArgs]))
    elif operation == "L":
        if len(subArgs) != 4:
            print("Draw Line usage example: L 1 2 6 2")
        else:
            canvas.draw_line(*[int(x) for x in subArgs])
    elif operation == "R":
        if len(subArgs) != 4:
            print("Draw Rectangle usage example: R 1 2 6 2")
        else:
            canvas.draw_rectangle(*[int(x) for x in subArgs])
    elif operation == "B":
        if len(subArgs) != 3:
            print("Fill usage example: B 10 3 s")
        else:
            canvas.fill(int(subArgs[0]), int(subArgs[1]), subArgs[2])
    elif operation == "Q":
        if len(subArgs) != 0:
            print("Quit syntax: Q")
        else:
            return (True, canvas)
    else:
        print("Command not supported")
    return (False, canvas)


loopBreak = False
currentCanvas = None

while not loopBreak:
    command = input("enter command: ")
    (loopBreak, currentCanvas) = command_selector(currentCanvas, command)
    if currentCanvas is not None:
        currentCanvas.print()
