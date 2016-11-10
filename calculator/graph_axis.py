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

import Tkinter as tk

behind_canvas_color = "grey"
grid_line_color = "cyan"
axis_line_color = "black"

def create_canvas(parent, width, height):
        canvas = tk.Canvas(parent, width=width, height=height);
        canvas.pack(fill=tk.BOTH, expand=1)
        return canvas

def draw_graph_background(canvas, event):
    canvas.delete('all')
    w, h = event.width, event.height
    step_x = w/6
    step_y = h/6


    # Draw Grid Lines
    i = 0
    while (i * step_x < w or i * step_y < h):
        canvas.create_line(i * step_x, 0, i * step_x, h, fill=grid_line_color)
        canvas.create_line(0,i * step_y, w, i * step_y, fill=grid_line_color)
        i += 1
    canvas.create_rectangle(0, 0, w, h, width=10, outline=behind_canvas_color)


    # Draw Axis Lines
    canvas.create_line(0, h/2, w, h/2, width=2, fill=axis_line_color)
    canvas.create_line(w/2, 0, w/2, h, width=2, fill=axis_line_color)
    ## Create Marker Points
    i=0
    points = [-3,-2,-1,0,1,2,3]
    while(i * step_x < w or i * step_y < h):
        canvas.create_line(i * step_x, h/2 - 5, i * step_x, h/2 + 5, width=1.5, fill=axis_line_color)
        canvas.create_line(w/2 - 5, i * step_y, w/2 + 5, i * step_y, width=1.5, fill=axis_line_color)

        #### Axis Lables
        canvas.create_text(i * step_x, h/2 + 15, text=str(points[i]))
        canvas.create_text(w/2 - 15, i * step_y, text=str(points[6-i]))
        i+=1

def main():
    root = tk.Tk()
    width=200
    height=200
    canvas = create_canvas(root, width, height)
    canvas.bind("<Configure>", lambda e: draw_graph_background(canvas, e))
    root.mainloop()

if __name__ == '__main__':
    main()
