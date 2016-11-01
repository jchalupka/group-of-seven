#!/usr/bin/python

from Tkinter import *
from tkFont import *

MIN_SIZE_PIXELS = 55
MAX_ROWS = 11
MAX_COLS = 14
GROUP_COLS = 4 # group widgets in sets of four columns

# sets column width and allows for window resizing
def configure_grid(root):
    for column in range(MAX_COLS):
        root.columnconfigure(column, minsize=MIN_SIZE_PIXELS, weight=1)
        for row in range(MAX_ROWS):
            root.rowconfigure(row, weight=1)

def add_to_entry(root, text):
    entry = root.focus_get()
    entry.insert(END, text)

def clear_entry(root):
    entry = root.focus_get()
    entry.delete(0, END)

def get_answer(equation):
    return eval(equation)

def execute_entry(root):
    entry = root.focus_get()
    equation = entry.get()
    answer = get_answer(equation)
    add_to_entry(root, "=")
    add_to_entry(root, answer)

def create_widgets(root):
    entry1_label = Label(root, text="1")
    entry2_label = Label(root, text="2")
    entry3_label = Label(root, text="3")
    entry4_label = Label(root, text="4")
    entry5_label = Label(root, text="5")
    entry6_label = Label(root, text="6")
    entry7_label = Label(root, text="7")

    entry1 = Entry(root, justify=RIGHT)
    entry2 = Entry(root, justify=RIGHT)
    entry3 = Entry(root, justify=RIGHT)
    entry4 = Entry(root, justify=RIGHT)
    entry5 = Entry(root, justify=RIGHT)
    entry6 = Entry(root, justify=RIGHT)
    entry7 = Entry(root, justify=RIGHT)

    entry1.focus_set()

    # must use lambdas to have parameters in the function that command is set to
    x = Button(root, text="x", command=lambda:add_to_entry(root, "x"))
    y = Button(root, text="y", command=lambda:add_to_entry(root, "y"))
    square = Button(root, text=u"a\u00B2", command=lambda:add_to_entry(root, "^2"))
    power = Button(root, text=u"a\u207F", command=lambda:add_to_entry(root, "^"))

    open_parens = Button(root, text="(", command=lambda:add_to_entry(root, "("))
    close_parens = Button(root, text=")", command=lambda:add_to_entry(root, ")"))
    less_than = Button(root, text="<", command=lambda:add_to_entry(root, "<"))
    greater_than = Button(root, text=">", command=lambda:add_to_entry(root, ">"))

    absolute = Button(root, text="|a|", command=lambda:add_to_entry(root, "abs"))
    pi = Button(root, text=u"\u03C0", command=lambda:add_to_entry(root, "pi"))
    less_than_equal = Button(root, text=u"\u2264", command=lambda:add_to_entry(root, "<="))
    greater_than_equal = Button(root, text=u"\u2265", command=lambda:add_to_entry(root, ">="))

    square_root = Button(root, text=u"\u221A", command=lambda:add_to_entry(root, "sqrt"))
    n_root = Button(root, text=u"\u221A", command=lambda:add_to_entry(root, "root"))
    remainder= Button(root, text=u"\uFE6A", command=lambda:add_to_entry(root, "%"))
    e = Button(root, text="e", command=lambda:add_to_entry(root, "e"))

    seven = Button(root, text="7", command=lambda:add_to_entry(root, "7"))
    eight = Button(root, text="8", command=lambda:add_to_entry(root, "8"))
    nine = Button(root, text="9", command=lambda:add_to_entry(root, "9"))
    divide = Button(root, text=u"\u00F7", command=lambda:add_to_entry(root, "/"))

    four = Button(root, text="4", command=lambda:add_to_entry(root, "4"))
    five = Button(root, text="5", command=lambda:add_to_entry(root, "5"))
    six = Button(root, text="6", command=lambda:add_to_entry(root, "6"))
    multiply = Button(root, text=u"\u00D7", command=lambda:add_to_entry(root, "*"))

    one = Button(root, text="1", command=lambda:add_to_entry(root, "1"))
    two = Button(root, text="2", command=lambda:add_to_entry(root, "2"))
    three = Button(root, text="3", command=lambda:add_to_entry(root, "3"))
    subtract = Button(root, text=u"\u2212", command=lambda:add_to_entry(root, "-"))

    zero = Button(root, text="0", command=lambda:add_to_entry(root, "0"))
    decimal = Button(root, text=".", command=lambda:add_to_entry(root, "."))
    negative = Button(root, text=u"(\u2212)", command=lambda:add_to_entry(root, "-"))
    add = Button(root, text="+", command=lambda:add_to_entry(root, "+"))

    go = Button(root, text="=", command=lambda:execute_entry(root))

    # fill grid
    entry1_label.grid(row=0, column=0)
    entry2_label.grid(row=1, column=0)
    entry3_label.grid(row=2, column=0)
    entry4_label.grid(row=3, column=0)
    entry5_label.grid(row=4, column=0)
    entry6_label.grid(row=5, column=0)
    entry7_label.grid(row=6, column=0)

    entry1.grid(row=0, column=1, columnspan=GROUP_COLS, sticky=W+E)
    entry2.grid(row=1, column=1, columnspan=GROUP_COLS, sticky=W+E)
    entry3.grid(row=2, column=1, columnspan=GROUP_COLS, sticky=W+E)
    entry4.grid(row=3, column=1, columnspan=GROUP_COLS, sticky=W+E)
    entry5.grid(row=4, column=1, columnspan=GROUP_COLS, sticky=W+E)
    entry6.grid(row=5, column=1, columnspan=GROUP_COLS, sticky=W+E)
    entry7.grid(row=6, column=1, columnspan=GROUP_COLS, sticky=W+E)

    x.grid(row=8, column=1, sticky=W+E)
    y.grid(row=8, column=2, sticky=W+E)
    square.grid(row=8, column=3, sticky=W+E)
    power.grid(row=8, column=4, sticky=W+E)
                   
    open_parens.grid(row=9, column=1, sticky=W+E)
    close_parens.grid(row=9, column=2, sticky=W+E)
    less_than.grid(row=9, column=3, sticky=W+E)
    greater_than.grid(row=9, column=4, sticky=W+E)

    absolute.grid(row=10, column=1, sticky=W+E)
    pi.grid(row=10, column=2, sticky=W+E)
    less_than_equal.grid(row=10, column=3, sticky=W+E)
    greater_than_equal.grid(row=10, column=4, sticky=W+E)

    square_root.grid(row=11, column=1, sticky=W+E)
    n_root.grid(row=11, column=2, sticky=W+E)
    remainder.grid(row=11, column=3, sticky=W+E)
    e.grid(row=11, column=4, sticky=W+E)

    seven.grid(row=8, column=6, sticky=W+E)
    eight.grid(row=8, column=7, sticky=W+E)
    nine.grid(row=8, column=8, sticky=W+E)
    divide.grid(row=8, column=9, sticky=W+E)

    four.grid(row=9, column=6, sticky=W+E)
    five.grid(row=9, column=7, sticky=W+E)
    six.grid(row=9, column=8, sticky=W+E)
    multiply.grid(row=9, column=9, sticky=W+E)

    one.grid(row=10, column=6, sticky=W+E)
    two.grid(row=10, column=7, sticky=W+E)
    three.grid(row=10, column=8, sticky=W+E)
    subtract.grid(row=10, column=9, sticky=W+E)

    zero.grid(row=11, column=6, sticky=W+E)
    decimal.grid(row=11, column=7, sticky=W+E)
    negative.grid(row=11, column=8, sticky=W+E)
    add.grid(row=11, column=9, sticky=W+E)

    go.grid(row=8, column=13, columnspan=2, rowspan=4, sticky=W+E)


def main():
    root = Tk()

    configure_grid(root)
    create_widgets(root)

    root.mainloop()

if __name__ == '__main__':
    main()
