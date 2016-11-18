#!/usr/bin/python

#
# Jorda Chalupka
#
# Last Edit Nov 2, 2016
#
# Should be able to add this into the GUI like a Button.
#
# There's still a lot of work to be done but I wanted to get this out in case
# there was any issue adding the canvas background to the GUI.
#
# Feel free to edit anything or work away on pieces.
#
from __future__ import division
from math import *
from decimal import *
import Tkinter as tk
# import translation



behind_canvas_color = "grey"
grid_line_color = "cyan"
axis_line_color = "black"

rangeVal = 1


# sets column width and allows for window resizing
def configure_grid(root):
    for column in range(MAX_COLS):
        root.columnconfigure(column, minsize=MIN_SIZE_PIXELS, weight=1)
        for row in range(MAX_ROWS):
            root.rowconfigure(row, weight=1)

def create_marker_points(canvas, w, h, step_x, step_y,max_range):
    i=0
    print max_range
    print "In graph " + str(max_range)
    points = [-3,-2,-1,0,1,2,3]
    points=[x*max_range for x in points]
    print points

    while(i * step_x < w or i * step_y < h):
        canvas.create_line(i * step_x, h/2 - 5, i * step_x, h/2 + 5, width=1.5, fill=axis_line_color, tags="background")
        canvas.create_line(w/2 - 5, i * step_y, w/2 + 5, i * step_y, width=1.5, fill=axis_line_color, tags="background")

        # Axis Labels
        canvas.create_text(i * step_x, h/2 + 15, text=str(points[i]), tags="background")
        canvas.create_text(w/2 - 15, i * step_y, text=str(points[6-i]), tags="background")
        i+=1


def draw_grid_lines(canvas, w, h, step_x, step_y):
    i = 0
    while i * step_x < w or i * step_y < h:
        canvas.create_line(i * step_x, 0, i * step_x, h, fill=grid_line_color, tags="background")
        canvas.create_line(0,i * step_y, w, i * step_y, fill=grid_line_color, tags="background")
        i += 1
    canvas.create_rectangle(0, 0, w, h, width=10, outline=behind_canvas_color, tags="background")

def draw_axis_lines(canvas, w, h):
    canvas.create_line(0, h/2, w, h/2, width=2, fill=axis_line_color, tags="background")
    canvas.create_line(w/2, 0, w/2, h, width=2, fill=axis_line_color, tags="background")

def create_canvas(parent, width, height):
        canvas = tk.Canvas(parent, width=width, height=height);
        canvas.pack(fill=tk.BOTH, expand=1)
        return canvas

def draw_graph_backgroundButton(canvas, max_range):
    canvas.delete('background')

    w, h = int(canvas.winfo_width()), int(canvas.winfo_height())
    step_x = w/6
    step_y = h/6

    draw_grid_lines(canvas, w, h, step_x, step_y)
    draw_axis_lines(canvas, w, h)
    create_marker_points(canvas, w, h, step_x, step_y,max_range)




def draw_graph_background(canvas, event, max_range):
    canvas.delete('background')
    w, h = event.width, event.height
    step_x = w/6
    step_y = h/6

    draw_grid_lines(canvas, w, h, step_x, step_y)
    draw_axis_lines(canvas, w, h)
    create_marker_points(canvas, w, h, step_x, step_y,max_range)




def draw_line(canvas, event, line):
    canvas.delete('line')
    w, h = event.width, event.height

    num_breaks = 6
    length_of_unit_w = w/num_breaks
    length_of_unit_h = h/num_breaks

    circle_size = 3

    for point in line:
        x,y = point[0], point[1]

        x = (w/2) + (length_of_unit_w * x)
        y = (h/2) - (length_of_unit_h * y)

        canvas.create_oval(
            x-circle_size/2,
            y-circle_size/2,
            x+circle_size/2,
            y+circle_size/2, fill='red', tags='line')
    canvas.tag_raise('line')



def window_resize(canvas, e, line):
    draw_graph_background(canvas, e)
    draw_line(canvas, e, line)



def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += Decimal(jump)


def pixels_per():
    # Calculate the number of pixels per unit we will need
    # eg. For smaller domains we will need more pixels per unit
    pixels_per = 25
    return pixels_per

def generate_line(function):
    #In future we should make a function that connects points and draws line segments insead of circles, maybe
    line = list((x,1) for x in drange(-10,10, 1/pixels_per()))

    # This part will actually come from the function the user enters, this is just for a simple test
    line = map(function, line)
    return line

def main():
    root = tk.Tk()
    width=200
    height=200

    # This part will actually come from the function the user enters, this is just for a simple test
    function = lambda x: (x[0],sin(x[0]*2))

    canvas = create_canvas(root, width, height)
    canvas.bind("<Configure>", lambda e: window_resize(canvas, e, generate_line(function)))
    root.mainloop()

if __name__ == '__main__':
    main()
