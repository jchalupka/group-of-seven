#!/usr/bin/python

from __future__ import division
import Tkinter as tk
import tkMessageBox as tkmsg
import sys
import command_line
import curve_drawer
import processing
import graph_axis

MIN_SIZE_PIXELS = 55
MAX_ROWS = 11
MAX_COLS = 14
GROUP_COLS = 4  # group widgets in sets of four columns

behind_canvas_color = "grey"
grid_line_color = "cyan"
axis_line_color = "black"


def get_points():
    import processing
    return processing.points


def set_points(new_points):
    import processing
    processing.points = new_points


def get_range():
    import graph_axis
    return graph_axis.rangeVal


def set_range(val):
    import graph_axis
    graph_axis.rangeVal = val


def range_increment():
    rangeVal = get_range()
    temp = rangeVal*2.0
    if(rangeVal < 32):
        if(temp >= 1.0):
            temp = int(temp)
        set_range(temp)

    print "Range: " + str(rangeVal)


def range_decrement():
    rangeVal = get_range()
    temp = rangeVal
    temp = temp / 2.0
    if(temp > 0):
        if(temp >= 1.0):
            temp = int(temp)
        set_range(temp)
    print "Range: " + str(rangeVal)


def execute_entry(root):
    entry = root.focus_get()
    expression = entry.get()

    result = processing.evaluate_expression(expression, get_range()*100)
    try:
        float(result)
        add_to_entry(root, " = ")
        add_to_entry(root, result)
    except ValueError:
        tkmsg.showinfo("Attention", result)
    except TypeError:
        set_points(result)


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


def set_function(root, text):
    entry = root.focus_lastfor()
    entry.insert(tk.END, text)


def buttonPressed(canvas, e, line, direction):
    if direction is 1:
        range_increment()
    elif direction is -1:
        range_decrement()

    max_range = get_range()
    graph_axis.draw_graph_backgroundButton(canvas, max_range)
    curve_drawer.draw_curveButton(canvas, line, max_range)


def window_resize(canvas, e, line):
    max_range = get_range()
    graph_axis.draw_graph_background(canvas, e, max_range)
    curve_drawer.draw_curve(canvas, e, line, max_range)


def function_window(root):
    top = tk.Toplevel(master=root)
    top.geometry('+955+100')

    # Trigometric Functions
    sin_button = tk.Button(top, text="SIN",
                           highlightbackground="DarkOrange1",
                           command=lambda: set_function(root, "sin"))
    cos_button = tk.Button(top, text="COS",
                           highlightbackground="DarkOrange1",
                           command=lambda: set_function(root, "cos"))
    tan_button = tk.Button(top, text="TAN",
                           highlightbackground="DarkOrange1",
                           command=lambda: set_function(root, "tan"))
    asin_button = tk.Button(top, text="ASIN",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "asin"))
    acos_button = tk.Button(top, text="ACOS",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "acos"))
    atan_button = tk.Button(top, text="ATAN",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "atan"))

    sin_button.grid(row=1, column=0, ipady=5, sticky=tk.N+tk.W+tk.E)
    cos_button.grid(row=2, column=0, ipady=5, sticky=tk.N+tk.W+tk.E)
    tan_button.grid(row=3, column=0, ipady=5, sticky=tk.N+tk.W+tk.E)
    asin_button.grid(row=4, column=0, ipady=5, sticky=tk.N+tk.W+tk.E)
    acos_button.grid(row=5, column=0, ipady=5, sticky=tk.N+tk.W+tk.E)
    atan_button.grid(row=6, column=0, ipady=5, sticky=tk.N+tk.W+tk.E)

    # Hyperbolic Functions
    sinh_button = tk.Button(top, text="SINH",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "sinh"))
    cosh_button = tk.Button(top, text="COSH",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "cosh"))
    tanh_button = tk.Button(top, text="TANH",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "tanh"))
    asinh_button = tk.Button(top, text="ASINH",
                             highlightbackground="DarkOrange1",
                             command=lambda: set_function(root, "asinh"))
    acosh_button = tk.Button(top, text="ACOSH",
                             highlightbackground="DarkOrange1",
                             command=lambda: set_function(root, "acosh"))
    atanh_button = tk.Button(top, text="ATANH",
                             highlightbackground="DarkOrange1",
                             command=lambda: set_function(root, "atanh"))

    sinh_button.grid(row=1, column=1, ipady=5, sticky=tk.N+tk.W+tk.E)
    cosh_button.grid(row=2, column=1, ipady=5, sticky=tk.N+tk.W+tk.E)
    tanh_button.grid(row=3, column=1, ipady=5, sticky=tk.N+tk.W+tk.E)
    asinh_button.grid(row=4, column=1, ipady=5, sticky=tk.N+tk.W+tk.E)
    acosh_button.grid(row=5, column=1, ipady=5, sticky=tk.N+tk.W+tk.E)
    atanh_button.grid(row=6, column=1, ipady=5, sticky=tk.N+tk.W+tk.E)

    # Number-theoretic and representation functions
    ceil_button = tk.Button(top, text="CEIL",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "ceil"))
    floor_button = tk.Button(top, text="FLOOR",
                             highlightbackground="DarkOrange1",
                             command=lambda: set_function(root, "floor"))
    abs_button = tk.Button(top, text="ABS", highlightbackground="DarkOrange1",
                           command=lambda: set_function(root, "abs"))

    ceil_button.grid(row=1, column=2, ipady=5, sticky=tk.N+tk.W+tk.E)
    floor_button.grid(row=2, column=2, ipady=5, sticky=tk.N+tk.W+tk.E)
    abs_button.grid(row=3, column=2, ipady=5, sticky=tk.N+tk.W+tk.E)

    # Power and logarithmic functions
    sqrt_button = tk.Button(top, text="SQRT",
                            highlightbackground="DarkOrange1",
                            command=lambda: set_function(root, "sqrt"))
    log_button = tk.Button(top, text="LOG",
                           highlightbackground="DarkOrange1",
                           command=lambda: set_function(root, "log"))
    ln_button = tk.Button(top, text="LN", highlightbackground="DarkOrange1",
                          command=lambda: set_function(root, "ln"))

    sqrt_button.grid(row=4, column=2, ipady=5, sticky=tk.N+tk.W+tk.E)
    log_button.grid(row=5, column=2, ipady=5, sticky=tk.N+tk.W+tk.E)
    ln_button.grid(row=6, column=2, ipady=5, sticky=tk.N+tk.W+tk.E)


def create_widgets(root):

    def load_file(root, text):
        fpt = open('input.txt', 'r')
        dataFile = fpt.read()
        myList = dataFile.split('\n')
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
        data = open('input.txt', 'w')
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

    entry1_label = tk.Label(root, text="1", width=6, bg="white smoke")
    entry2_label = tk.Label(root, text="2", width=6, bg="white smoke")
    entry3_label = tk.Label(root, text="3", width=6, bg="white smoke")
    entry4_label = tk.Label(root, text="4", width=6, bg="white smoke")
    entry5_label = tk.Label(root, text="5", width=6, bg="white smoke")
    entry6_label = tk.Label(root, text="6", width=6, bg="white smoke")
    entry7_label = tk.Label(root, text="7", width=6, bg="white smoke")

    entry1 = tk.Entry(root, justify=tk.RIGHT,
                      highlightbackground="white smoke")
    entry2 = tk.Entry(root, justify=tk.RIGHT,
                      highlightbackground="white smoke")
    entry3 = tk.Entry(root, justify=tk.RIGHT,
                      highlightbackground="white smoke")
    entry4 = tk.Entry(root, justify=tk.RIGHT,
                      highlightbackground="white smoke")
    entry5 = tk.Entry(root, justify=tk.RIGHT,
                      highlightbackground="white smoke")
    entry6 = tk.Entry(root, justify=tk.RIGHT,
                      highlightbackground="white smoke")
    entry7 = tk.Entry(root, justify=tk.RIGHT,
                      highlightbackground="white smoke")

    entry1.focus_set()
    canvas = tk.Canvas(root, width=400, height=370)

    x = tk.Button(root, text="x", highlightbackground="gray39",
                  command=lambda: add_to_entry(root, "x"))
    y = tk.Button(root, text="y", highlightbackground="gray39",
                  command=lambda: add_to_entry(root, "y"))
    square = tk.Button(root, text=u"a\u00B2", highlightbackground="gray39",
                       command=lambda: add_to_entry(root, "^2"))
    power = tk.Button(root, text=u"a\u207F", highlightbackground="gray39",
                      command=lambda: add_to_entry(root, "^"))

    open_parens = tk.Button(root, text="(", highlightbackground="gray39",
                            command=lambda: add_to_entry(root, "("))
    close_parens = tk.Button(root, text=")", highlightbackground="gray39",
                             command=lambda: add_to_entry(root, ")"))
    ceil = tk.Button(root, text=u"\u2308\u2309", highlightbackground="gray39",
                     command=lambda: add_to_entry(root, "ceil"))
    floor = tk.Button(root, text=u"\u230A\u230B", highlightbackground="gray39",
                      command=lambda: add_to_entry(root, "floor"))

    absolute = tk.Button(root, text="|a|", highlightbackground="gray39",
                         command=lambda: add_to_entry(root, "abs"))
    pi = tk.Button(root, text=u"\u03C0", highlightbackground="gray39",
                   command=lambda: add_to_entry(root, "pi"))
    log = tk.Button(root, text="log", highlightbackground="gray39",
                    command=lambda: add_to_entry(root, "log"))
    ln = tk.Button(root, text="ln", highlightbackground="gray39",
                   command=lambda: add_to_entry(root, "ln"))

    square_root = tk.Button(root, text=u"\u221A", highlightbackground="gray39",
                            command=lambda: add_to_entry(root, "sqrt"))
    factorial = tk.Button(root, text="n!", highlightbackground="gray39",
                          command=lambda: add_to_entry(root, "!"))
    remainder = tk.Button(root, text=u"\uFE6A", highlightbackground="gray39",
                          command=lambda: add_to_entry(root, "%"))
    e = tk.Button(root, text="e", highlightbackground="gray39",
                  command=lambda: add_to_entry(root, "e"))

    seven = tk.Button(root, text="7", highlightbackground="DarkOrange1",
                      command=lambda: add_to_entry(root, "7"))
    eight = tk.Button(root, text="8", highlightbackground="DarkOrange1",
                      command=lambda: add_to_entry(root, "8"))
    nine = tk.Button(root, text="9", highlightbackground="DarkOrange1",
                     command=lambda: add_to_entry(root, "9"))
    divide = tk.Button(root, text=u"\u00F7", highlightbackground="DarkOrange1",
                       command=lambda: add_to_entry(root, "/"))
    function_button = tk.Button(root, text="Functions",
                                highlightbackground="gray",
                                command=lambda: function_window(root))

    four = tk.Button(root, text="4", highlightbackground="DarkOrange1",
                     command=lambda: add_to_entry(root, "4"))
    five = tk.Button(root, text="5", highlightbackground="DarkOrange1",
                     command=lambda: add_to_entry(root, "5"))
    six = tk.Button(root, text="6", highlightbackground="DarkOrange1",
                    command=lambda: add_to_entry(root, "6"))
    multiply = tk.Button(root, text=u"\u00D7",
                         highlightbackground="DarkOrange1",
                         command=lambda: add_to_entry(root, "*"))

    one = tk.Button(root, text="1", highlightbackground="DarkOrange1",
                    command=lambda: add_to_entry(root, "1"))
    two = tk.Button(root, text="2", highlightbackground="DarkOrange1",
                    command=lambda: add_to_entry(root, "2"))
    three = tk.Button(root, text="3", highlightbackground="DarkOrange1",
                      command=lambda: add_to_entry(root, "3"))
    subtract = tk.Button(root, text=u"\u2212",
                         highlightbackground="DarkOrange1",
                         command=lambda: add_to_entry(root, "-"))

    # Range up and down buttons, they call imported functions in graph_axis
    range_up = tk.Button(root, text=u"\u2191", highlightbackground="gray75")
    range_down = tk.Button(root, text=u"\u2193", highlightbackground="gray75")
    range_label = tk.Label(root, text="Range", bg="grey75")
    range_up.bind("<Button-1>",
                  lambda e: buttonPressed(canvas, e, get_points(), 1))
    range_down.bind("<Button-1>",
                    lambda e: buttonPressed(canvas, e, get_points(), -1))

    zero = tk.Button(root, text="0", highlightbackground="DarkOrange1",
                     command=lambda: add_to_entry(root, "0"))
    decimal = tk.Button(root, text=".", highlightbackground="DarkOrange1",
                        command=lambda: add_to_entry(root, "."))
    negative = tk.Button(root, text=u"(\u2212)",
                         highlightbackground="DarkOrange1",
                         command=lambda: add_to_first(root, "-"))
    add = tk.Button(root, text="+", highlightbackground="DarkOrange1",
                    command=lambda: add_to_entry(root, "+"))
    clear = tk.Button(root, text="Clear", highlightbackground="gray39",
                      command=lambda: clear_entry(root))

    go = tk.Button(root, text="=", highlightbackground="gray39")
    go.bind("<Button-1>",
            lambda e: curve_drawer.show_new_line(canvas, get_range()))

    load = tk.Button(root, text="Load", highlightbackground="gray75",
                     command=lambda: load_file(root, "Load"))
    save = tk.Button(root, text="Save", highlightbackground="gray75",
                     command=lambda: save_file(root, "Save"))

    # fill grid
    entry1_label.grid(row=1, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry2_label.grid(row=2, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry3_label.grid(row=3, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry4_label.grid(row=4, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry5_label.grid(row=5, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry6_label.grid(row=6, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)
    entry7_label.grid(row=7, column=0, ipady=16, sticky=tk.N+tk.W+tk.E)

    entry1.grid(row=1, column=1, columnspan=GROUP_COLS, ipady=13,
                sticky=tk.N+tk.W+tk.E)
    entry2.grid(row=2, column=1, columnspan=GROUP_COLS, ipady=13,
                sticky=tk.N+tk.W+tk.E)
    entry3.grid(row=3, column=1, columnspan=GROUP_COLS, ipady=13,
                sticky=tk.N+tk.W+tk.E)
    entry4.grid(row=4, column=1, columnspan=GROUP_COLS, ipady=13,
                sticky=tk.N+tk.W+tk.E)
    entry5.grid(row=5, column=1, columnspan=GROUP_COLS, ipady=13,
                sticky=tk.N+tk.W+tk.E)
    entry6.grid(row=6, column=1, columnspan=GROUP_COLS, ipady=13,
                sticky=tk.N+tk.W+tk.E)
    entry7.grid(row=7, column=1, columnspan=GROUP_COLS, ipady=13,
                sticky=tk.N+tk.W+tk.E)

    canvas.grid(row=1, column=5, columnspan=9, rowspan=7,
                sticky=tk.N+tk.E+tk.S+tk.W)
    canvas.bind("<Configure>",
                lambda e: window_resize(canvas, e, get_points()))

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
    function_button.grid(row=13, column=6, columnspan=2, rowspan=2, ipadx=15,
                         ipady=24, sticky=tk.W+tk.E)

    zero.grid(row=12, column=6, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    decimal.grid(row=12, column=7, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    negative.grid(row=12, column=8, ipadx=15, ipady=5, sticky=tk.W+tk.E)
    add.grid(row=12, column=9, ipadx=15, ipady=5, sticky=tk.W+tk.E)

    # buttons and labels for ranges
    range_up.grid(row=10, column=11, ipadx=8, ipady=2, sticky=tk.W+tk.E)
    range_down.grid(row=11, column=11, ipadx=8, ipady=2, sticky=tk.W+tk.E)
    range_label.grid(row=9, column=10, columnspan=3, sticky=tk.W+tk.E)

    clear.grid(row=9, column=13, columnspan=2, rowspan=2, ipadx=15, ipady=24,
               sticky=tk.W+tk.E)
    load.grid(row=13, column=1, columnspan=2, rowspan=2, ipadx=15, ipady=24,
              sticky=tk.W+tk.E)
    go.grid(row=11, column=13, columnspan=2, rowspan=2, ipadx=15, ipady=24,
            sticky=tk.W+tk.E)
    save.grid(row=13, column=3, columnspan=2, rowspan=2, ipadx=15, ipady=24,
              sticky=tk.W+tk.E)


def main():
    if len(sys.argv) == 1:
        root = tk.Tk()
        root.configure(bg="gray75")
        configure_grid(root)
        create_widgets(root)
        root.mainloop()
    elif len(sys.argv) == 2:
        command_line.evaluate_from_file(sys.argv[1])
    else:
        sys.exit("Error. Invalid number of arguments.")

if __name__ == '__main__':
    main()
