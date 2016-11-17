#!/usr/bin/python

import Tkinter as tk
import sys
import commandLine
import curve_drawer
import expression_validator
from graph_axis import rangeIncre, rangeDecre


MIN_SIZE_PIXELS = 55
MAX_ROWS = 11
MAX_COLS = 14
GROUP_COLS = 4 # group widgets in sets of four columns

behind_canvas_color = "grey"
grid_line_color = "cyan"
axis_line_color = "black"

global rangeVal
rangeVal = 8

def rangeIncre():
    global rangeVal
    temp = rangeVal
    temp = temp*2
    if(temp<9223372036854775807):
        rangeVal = temp
        print "Range: " + str(rangeVal)


def rangeDecre():
    global rangeVal
    temp = rangeVal
    temp = temp/2
    if(temp>0):
        rangeVal = temp
    print "Range: " + str(rangeVal)

# sets column width and allows for window resizing
def configure_grid(root):
    for column in range(MAX_COLS):
        root.columnconfigure(column, minsize=MIN_SIZE_PIXELS, weight=1)
        for row in range(MAX_ROWS):
            root.rowconfigure(row, weight=1)

def add_to_entry(root, text):
    entry = root.focus_get()
    entry.insert(tk.END, text)

def add_to_first(root, text):
    entry = root.focus_get()
    entry.insert(tk.ANCHOR, text)

def clear_entry(root):
    entry = root.focus_get()
    entry.delete(0, tk.END)

def get_answer(equation):
    return eval(equation)

def update_status(status_bar, response):
    status_bar.config(text=response)

def execute_entry(root, status_bar):
    entry = root.focus_get()
    equation = entry.get()
    answer  = expression_validator.gui_function_validator(equation, status_bar)
    if answer is not None:
        add_to_entry(root, " = ")
        add_to_entry(root, answer)


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

def create_marker_points(canvas, w, h, step_x, step_y):
    i=0
    global rangeVal
    points = [-3,-2,-1,0,1,2,3]
    points=[x*rangeVal for x in points]

    while(i * step_x < w or i * step_y < h):
        canvas.create_line(i * step_x, h/2 - 5, i * step_x, h/2 + 5, width=1.5, fill=axis_line_color, tags="background")
        canvas.create_line(w/2 - 5, i * step_y, w/2 + 5, i * step_y, width=1.5, fill=axis_line_color, tags="background")

        # Axis Labels
        canvas.create_text(i * step_x, h/2 + 15, text=str(points[i]), tags="background")
        canvas.create_text(w/2 - 15, i * step_y, text=str(points[6-i]), tags="background")
        i+=1

def buttonPressed(canvas, e, line):
    draw_graph_backgroundButton(canvas)
    curve_drawer.draw_curveButton(canvas, line)

def draw_graph_backgroundButton(canvas):
    canvas.delete('background')

    w, h = int(canvas.winfo_width()), int(canvas.winfo_height())

    step_x = w/6
    step_y = h/6

    draw_grid_lines(canvas, w, h, step_x, step_y)
    draw_axis_lines(canvas, w, h)
    create_marker_points(canvas, w, h, step_x, step_y)

def draw_graph_background(canvas, event):
    canvas.delete('background')
    w, h = event.width, event.height
    step_x = w/6
    step_y = h/6

    draw_grid_lines(canvas, w, h, step_x, step_y)
    draw_axis_lines(canvas, w, h)
    create_marker_points(canvas, w, h, step_x, step_y)


def window_resize(canvas, e, line):
    draw_graph_background(canvas, e)
    curve_drawer.draw_curve(canvas, e, line)

def create_widgets(root):

    def load_file(root, text):
        fpt=open('input.txt', 'r')
        dataFile=fpt.read()
        myList=dataFile.split('\n')
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        entry4.delete(0, tk.END)
        entry5.delete(0, tk.END)
        entry6.delete(0, tk.END)
        entry7.delete(0, tk.END)

        entry1.insert(0, myList[0])
        entry2.insert(0, myList[1])
        entry3.insert(0, myList[2])
        entry4.insert(0, myList[3])
        entry5.insert(0, myList[4])
        entry6.insert(0, myList[5])
        entry7.insert(0, myList[6])

    def save_file(root, text):
        data=open('output.txt', 'w')
        data.write(entry1.get())
        data.write("\n")
        data.write(entry2.get())
        data.write("\n")
        data.write(entry3.get())
        data.write("\n")
        data.write(entry4.get())
        data.write("\n")
        data.write(entry5.get())
        data.write("\n")
        data.write(entry6.get())
        data.write("\n")
        data.write(entry7.get())

    status_bar = tk.Label(root, text="*", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    entry1_label = tk.Label(root, text="1", width=6, bg="white smoke")
    entry2_label = tk.Label(root, text="2", width=6, bg="white smoke")
    entry3_label = tk.Label(root, text="3", width=6, bg="white smoke")
    entry4_label = tk.Label(root, text="4", width=6, bg="white smoke")
    entry5_label = tk.Label(root, text="5", width=6, bg="white smoke")
    entry6_label = tk.Label(root, text="6", width=6, bg="white smoke")
    entry7_label = tk.Label(root, text="7", width=6, bg="white smoke")

    entry1 = tk.Entry(root, justify=tk.RIGHT,  highlightbackground="white smoke")
    entry2 = tk.Entry(root, justify=tk.RIGHT, highlightbackground="white smoke")
    entry3 = tk.Entry(root, justify=tk.RIGHT, highlightbackground="white smoke")
    entry4 = tk.Entry(root, justify=tk.RIGHT, highlightbackground="white smoke")
    entry5 = tk.Entry(root, justify=tk.RIGHT, highlightbackground="white smoke")
    entry6 = tk.Entry(root, justify=tk.RIGHT, highlightbackground="white smoke")
    entry7 = tk.Entry(root, justify=tk.RIGHT, highlightbackground="white smoke")

    entry1.focus_set()
    canvas = tk.Canvas(root, width=400, height=370)

    # must use lambdas to have parameters in the function that command is set to
    x = tk.Button(root, text="x", highlightbackground="gray39", command=lambda:add_to_entry(root, "x"))
    y = tk.Button(root, text="y", highlightbackground="gray39", command=lambda:add_to_entry(root, "y"))
    square = tk.Button(root, text=u"a\u00B2", highlightbackground="gray39", command=lambda:add_to_entry(root, "^2"))
    power = tk.Button(root, text=u"a\u207F", highlightbackground="gray39", command=lambda:add_to_entry(root, "^"))

    open_parens = tk.Button(root, text="(", highlightbackground="gray39", command=lambda:add_to_entry(root, "("))
    close_parens = tk.Button(root, text=")", highlightbackground="gray39", command=lambda:add_to_entry(root, ")"))
    ceil = tk.Button(root, text=u"\u2308\u2309", highlightbackground="gray39", command=lambda:add_to_entry(root, "ceil"))
    floor = tk.Button(root, text=u"\u230A\u230B", highlightbackground="gray39", command=lambda:add_to_entry(root, "floor"))

    absolute = tk.Button(root, text="|a|", highlightbackground="gray39", command=lambda:add_to_entry(root, "abs"))
    pi = tk.Button(root, text=u"\u03C0", highlightbackground="gray39", command=lambda:add_to_entry(root, "pi"))
    log = tk.Button(root, text="log", highlightbackground="gray39", command=lambda:add_to_entry(root, "log"))
    ln = tk.Button(root, text="ln", highlightbackground="gray39", command=lambda:add_to_entry(root, "ln"))

    square_root = tk.Button(root, text=u"\u221A", highlightbackground="gray39", command=lambda:add_to_entry(root, "sqrt"))
    factorial = tk.Button(root, text="n!", highlightbackground="gray39", command=lambda:add_to_entry(root, "!"))
    remainder= tk.Button(root, text=u"\uFE6A", highlightbackground="gray39", command=lambda:add_to_entry(root, "%"))
    e = tk.Button(root, text="e", highlightbackground="gray39", command=lambda:add_to_entry(root, "e"))

    seven = tk.Button(root, text="7", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "7"))
    eight = tk.Button(root, text="8", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "8"))
    nine = tk.Button(root, text="9", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "9"))
    divide = tk.Button(root, text=u"\u00F7", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "/"))

    four = tk.Button(root, text="4", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "4"))
    five = tk.Button(root, text="5", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "5"))
    six = tk.Button(root, text="6", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "6"))
    multiply = tk.Button(root, text=u"\u00D7", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "*"))

    one = tk.Button(root, text="1", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "1"))
    two = tk.Button(root, text="2", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "2"))
    three = tk.Button(root, text="3", highlightbackground="DarkOrange1",command=lambda:add_to_entry(root, "3"))
    subtract = tk.Button(root, text=u"\u2212", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "-"))

    #Range up and down buttons, they call imported functions in graph_axis
    rangeUp = tk.Button(root,text=u"\u2191 ", highlightbackground="gray75", command=lambda: rangeIncre())
    rangeDown = tk.Button(root,text=u"\u2193", highlightbackground="gray75",command=lambda: rangeDecre())
    rangeUp.bind("<Button-1>", lambda e: buttonPressed(canvas, e, curve_drawer.generate_line(function)))
    rangeDown.bind("<Button-1>", lambda e: buttonPressed(canvas, e, curve_drawer.generate_line(function)))

    zero = tk.Button(root, text="0", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "0"))
    decimal = tk.Button(root, text=".", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "."))
    negative = tk.Button(root, text=u"(\u2212)", highlightbackground="DarkOrange1", command=lambda:add_to_first(root, "-"))
    add = tk.Button(root, text="+", highlightbackground="DarkOrange1", command=lambda:add_to_entry(root, "+"))
    clear = tk.Button(root, text="Clear", highlightbackground="gray39", command=lambda:clear_entry(root))
    go = tk.Button(root, text="=", highlightbackground="gray39", command=lambda:execute_entry(root, status_bar))

    load = tk.Button(root, text="Load", highlightbackground="gray75", command=lambda:load_file(root, "Load"))
    save = tk.Button(root, text="Save", highlightbackground="gray75", command=lambda:save_file(root, "Save"))

    # fill grid
    entry1_label.grid(row=1, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry2_label.grid(row=2, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry3_label.grid(row=3, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry4_label.grid(row=4, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry5_label.grid(row=5, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry6_label.grid(row=6, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry7_label.grid(row=7, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)

    status_bar.grid(row=0, column=0, columnspan=MAX_COLS, sticky=tk.N+tk.E+tk.W)
    entry1.grid(row=1, column=1, columnspan=GROUP_COLS, ipady=13, sticky=tk.N+tk.W+tk.E)
    entry2.grid(row=2, column=1, columnspan=GROUP_COLS, ipady=13, sticky=tk.N+tk.W+tk.E)
    entry3.grid(row=3, column=1, columnspan=GROUP_COLS, ipady=13, sticky=tk.N+tk.W+tk.E)
    entry4.grid(row=4, column=1, columnspan=GROUP_COLS, ipady=13, sticky=tk.N+tk.W+tk.E)
    entry5.grid(row=5, column=1, columnspan=GROUP_COLS, ipady=13, sticky=tk.N+tk.W+tk.E)
    entry6.grid(row=6, column=1, columnspan=GROUP_COLS, ipady=13, sticky=tk.N+tk.W+tk.E)
    entry7.grid(row=7, column=1, columnspan=GROUP_COLS, ipady=13, sticky=tk.N+tk.W+tk.E)

    canvas.grid(row=1, column=5, columnspan=9, rowspan=7, sticky=tk.N+tk.E+tk.S+tk.W)
    # generate function should be replaced by a function that gets the function from the user, and processes, etc
    function = curve_drawer.generate_function()
    canvas.bind("<Configure>", lambda e: window_resize(canvas, e, curve_drawer.generate_line(function)))

    x.grid(row=9, column=1, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    y.grid(row=9, column=2, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    square.grid(row=9, column=3, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    power.grid(row=9, column=4, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    open_parens.grid(row=10, column=1, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    close_parens.grid(row=10, column=2, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    ceil.grid(row=10, column=3, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    floor.grid(row=10, column=4, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    absolute.grid(row=11, column=1, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    pi.grid(row=11, column=2, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    log.grid(row=11, column=3, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    ln.grid(row=11, column=4, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    square_root.grid(row=12, column=1, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    factorial.grid(row=12, column=2, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    remainder.grid(row=12, column=3, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    e.grid(row=12, column=4, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    seven.grid(row=9, column=6, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    eight.grid(row=9, column=7, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    nine.grid(row=9, column=8, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    divide.grid(row=9, column=9, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    four.grid(row=10, column=6, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    five.grid(row=10, column=7, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    six.grid(row=10, column=8, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    multiply.grid(row=10, column=9, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    one.grid(row=11, column=6, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    two.grid(row=11, column=7, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    three.grid(row=11, column=8, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    subtract.grid(row=11, column=9, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    zero.grid(row=12, column=6, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    decimal.grid(row=12, column=7, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    negative.grid(row=12, column=8, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    add.grid(row=12, column=9, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    #buttons and lables for ranges
    rangeUp.grid(row=10, column=11, ipadx=8, ipady=2,sticky=tk.W+tk.E)
    rangeDown.grid(row=11,column=11,ipadx=8, ipady=2,sticky=tk.W+tk.E)
    tk.Label(root, text="Range", bg = "grey75").grid(row=9,column=10, sticky=tk.W+tk.E)

    clear.grid(row=9, column=13, columnspan=2, rowspan=2, ipadx=15, ipady=24, sticky=tk.W+tk.E)
    load.grid(row=13, column=1, columnspan=2, rowspan=2, ipadx=15, ipady=24, sticky=tk.W+tk.E)
    go.grid(row=11, column=13, columnspan=2, rowspan=2, ipadx=15, ipady=24, sticky=tk.W+tk.E)
    save.grid(row=13, column=3, columnspan=2, rowspan=2, ipadx=15, ipady=24, sticky=tk.W+tk.E)

def main():
    if len(sys.argv) == 1:
        root = tk.Tk()
        root.configure(bg="gray75")
        configure_grid(root)
        create_widgets(root)
        root.mainloop()
    elif len(sys.argv) == 2:
        commandLine.main(sys,sys.argv[1])
    else:
        sys.exit("Error. Invalid number of arguments.")

if __name__ == '__main__':
    main()
