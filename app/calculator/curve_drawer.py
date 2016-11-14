# Curve drawing

#!/usr/bin/python
from __future__ import division
import decimal
import math
import Tkinter as tk

def line_maker(points):
	first = True
	p_x = p_y = 0

	for (x,y) in points:
		if first:
			p_x = x
			p_y = y
			first = False
		else:
			yield p_x, p_y, x, y
			p_x = x
			p_y = y

def draw_curve(canvas, event, line):
	canvas.delete('line')

	w, h = event.width, event.height

	num_breaks = 6
	length_of_unit_w = w/num_breaks
	length_of_unit_h = h/num_breaks
	for (x1, y1, x2, y2) in line_maker(line):
		x1 = (w/2) + (length_of_unit_w * x1)
		x2 = (w/2) + (length_of_unit_w * x2)
		y1 = (h/2) - (length_of_unit_h * y1)
		y2 = (h/2) - (length_of_unit_h * y2)
		canvas.create_line(x1, y1, x2, y2, width=1, tags='line')

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

