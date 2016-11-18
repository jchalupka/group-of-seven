#!/usr/bin/python

from __future__ import division
import calculator_gui
from math import *
from decimal import *
import Tkinter as tk


behind_canvas_color = "grey"
grid_line_color = "cyan"
axis_line_color = "black"

range_value = 1.0


def check_range(points):
    newList = []
    counter = 0
    for i in points:
        if counter < 3:
            if i < -1000 or i > -0.05:
                newList.append('{:.1e}'.format(float(i)))
            else:
                newList.append(i)
        elif counter > 3:
            if i > 1000 or i < 0.05:
                newList.append('{:.1e}'.format(float(i)))
            else:
                newList.append(i)
        else:
            newList.append(i)
        counter += 1
    return newList


def create_marker_points(canvas, w, h, step_x, step_y, max_range):
    i = 0
    points = [-3, -2, -1, 0, 1, 2, 3]

    points = [x * max_range for x in points]

    while i * step_x < w or i * step_y < h:
        canvas.create_line(i * step_x, h / 2 - 5, i * step_x, h / 2 + 5,
                           width=1.5, fill=axis_line_color, tags="background")
        canvas.create_line(w / 2 - 5, i * step_y, w / 2 + 5, i * step_y,
                           width=1.5, fill=axis_line_color, tags="background")

        # Axis Labels
        canvas.create_text(i * step_x, h / 2 + 15, text=str(points[i]),
                           tags="background")
        canvas.create_text(w / 2 - 15, i * step_y, text=str(points[6 - i]),
                           tags="background")
        i += 1


def draw_grid_lines(canvas, w, h, step_x, step_y):
    i = 0
    while i * step_x < w or i * step_y < h:
        canvas.create_line(i * step_x, 0, i * step_x, h, fill=grid_line_color,
                           tags="background")
        canvas.create_line(0, i * step_y, w, i * step_y, fill=grid_line_color,
                           tags="background")
        i += 1
    canvas.create_rectangle(0, 0, w, h, width=10, outline=behind_canvas_color,
                            tags="background")


def draw_axis_lines(canvas, w, h):
    canvas.create_line(0, h / 2, w, h / 2, width=2, fill=axis_line_color,
                       tags="background")
    canvas.create_line(w / 2, 0, w / 2, h, width=2, fill=axis_line_color,
                       tags="background")


def create_canvas(parent, width, height):
        canvas = tk.Canvas(parent, width=width, height=height)
        canvas.pack(fill=tk.BOTH, expand=1)
        return canvas


def draw_graph_backgroundButton(canvas, max_range):
    canvas.delete('background')

    w, h = int(canvas.winfo_width()), int(canvas.winfo_height())
    step_x = w/6
    step_y = h/6

    draw_grid_lines(canvas, w, h, step_x, step_y)
    draw_axis_lines(canvas, w, h)
    create_marker_points(canvas, w, h, step_x, step_y, max_range)


def draw_graph_background(canvas, event, max_range):
    canvas.delete('background')
    w, h = event.width, event.height
    step_x = w/6
    step_y = h/6

    draw_grid_lines(canvas, w, h, step_x, step_y)
    draw_axis_lines(canvas, w, h)
    create_marker_points(canvas, w, h, step_x, step_y, max_range)


def window_resize(canvas, e, line):
    draw_graph_background(canvas, e, calculator_gui.get_points())
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
