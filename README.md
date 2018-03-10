# Canvas on terminal
This project presents a command line canvas solution that accepts the following commands: C, L, R, B, Q, usage details covered in the section *Usage Instructions*
## Run the solution
### prerequisites
- python 3
- venv (included with python 3 installation)
### run the solution
assuming your python 3 alias is *python3* (if not replace for yours) and that you're on a UNIX based OS, from the root of the repository execute
```bash
>> python3 canvas/main.py
```

### run the unit tests
same assumptions as before, from the root of the repository execute
```bash
>> python3 -m venv env
>> source env/bin/activate # you should see env before the caret
(env) >> pip install -r requirements.txt
(env) >> pytest
```
## Usage instructions
### Create Canvas
`C <width> <height>`

Create a canvas with the given dimensions, the axis are represented as follows
```
------>x
|
|
|
v
y
```
### Draw Line
`L <x0> <y0> <x1> <y1>`

Draws a line with origin on (x0, y0) and destination on (x1, y1), the lines should be parallel to one of the axis or the command will be ignored

### Draw Rectangle
`R <x0> <y0> <x1> <y1>`

Draws a rectangle using the given points using the minimum of the x and y components as the upper left corner and the maxumum of the x and y components as the lower right corner

### Fill
`B <x0> <y0> <colour>`

Spread the *colour* from the point (x0, y0) horizontally and vertically stoping at the edge of the canvas or when encounters a line denoted by *x*

### Quit
`Q`

Exits the application.