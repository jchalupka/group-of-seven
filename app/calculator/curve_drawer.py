#!/usr/bin/python

from __future__ import division
import calculator_gui
import graph_axis
import decimal
import math
import Tkinter as tk


def show_new_line(root, max_range):
	calculator_gui.execute_entry(root)
	draw_curve_button(root, calculator_gui.get_points(), max_range)


def line_maker(points):
	first = True
	p_x = p_y = 0

	for (x, y) in points:
		if first:
			p_x = x
			p_y = y
			first = False
		else:
			yield p_x, p_y, x, y
			p_x = x
			p_y = y


def calc_height_width(canvas, line, max_range, h, w):
	num_breaks = 6 * max_range
	length_of_unit_w = w/num_breaks
	length_of_unit_h = h/num_breaks
	for (x1, y1, x2, y2) in line_maker(line):
		x1 = (w / 2) + (length_of_unit_w * x1)
		x2 = (w / 2) + (length_of_unit_w * x2)
		y1 = (h / 2) - (length_of_unit_h * y1)
		y2 = (h / 2) - (length_of_unit_h * y2)
		canvas.create_line(x1, y1, x2, y2, width=2, tags='line')


def draw_curve_button(canvas, line, max_range):
	canvas.delete('line')

	w, h = int(canvas.winfo_width()), int(canvas.winfo_height())
	calc_height_width(canvas, line, max_range, h, w)


def draw_curve(canvas, event, line, max_range):
	canvas.delete('line')

	w, h = int(event.width), int(event.height)

	calc_height_width(canvas, line, max_range, h, w)
