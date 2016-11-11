#!/usr/bin/env python

from __future__ import division

import Tkinter as tk
import decimal
import math

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

def pixels_per():
    # Calculate the number of pixels per unit we will need
    # eg. For smaller domains we will need more pixels per unit
    pixels_per = 25
    return pixels_per

def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)

def generate_line(function):
    #In future we should make a function that connects points and draws line segments insead of circles, maybe
    line = list((x,1) for x in drange(-10,10, 1/pixels_per()))

    # This part will actually come from the function the user enters, this is just for a simple test
    line = map(function, line)
    return line

# This is just temporary and will be replaced by a function that the user gives
def generate_function():
    function = lambda x: (x[0], math.sin(x[0]*2))
    return function
