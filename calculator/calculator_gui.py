#!/usr/bin/python

import Tkinter as tk

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
    entry1_label = tk.Label(root, text="1")
    entry2_label = tk.Label(root, text="2")
    entry3_label = tk.Label(root, text="3")
    entry4_label = tk.Label(root, text="4")
    entry5_label = tk.Label(root, text="5")
    entry6_label = tk.Label(root, text="6")
    entry7_label = tk.Label(root, text="7")

    entry1 = tk.Entry(root, justify=tk.RIGHT)
    entry2 = tk.Entry(root, justify=tk.RIGHT)
    entry3 = tk.Entry(root, justify=tk.RIGHT)
    entry4 = tk.Entry(root, justify=tk.RIGHT)
    entry5 = tk.Entry(root, justify=tk.RIGHT)
    entry6 = tk.Entry(root, justify=tk.RIGHT)
    entry7 = tk.Entry(root, justify=tk.RIGHT)

    entry1.focus_set()

    # must use lambdas to have parameters in the function that command is set to
    x = tk.Button(root, text="x", command=lambda:add_to_entry(root, "x"))
    y = tk.Button(root, text="y", command=lambda:add_to_entry(root, "y"))
    square = tk.Button(root, text=u"a\u00B2", command=lambda:add_to_entry(root, "^2"))
    power = tk.Button(root, text=u"a\u207F", command=lambda:add_to_entry(root, "^"))

    open_parens = tk.Button(root, text="(", command=lambda:add_to_entry(root, "("))
    close_parens = tk.Button(root, text=")", command=lambda:add_to_entry(root, ")"))
    less_than = tk.Button(root, text="<", command=lambda:add_to_entry(root, "<"))
    greater_than = tk.Button(root, text=">", command=lambda:add_to_entry(root, ">"))

    absolute = tk.Button(root, text="|a|", command=lambda:add_to_entry(root, "abs"))
    pi = tk.Button(root, text=u"\u03C0", command=lambda:add_to_entry(root, "pi"))
    less_than_equal = tk.Button(root, text=u"\u2264", command=lambda:add_to_entry(root, "<="))
    greater_than_equal = tk.Button(root, text=u"\u2265", command=lambda:add_to_entry(root, ">="))

    square_root = tk.Button(root, text=u"\u221A", command=lambda:add_to_entry(root, "sqrt"))
    n_root = tk.Button(root, text=u"\u221A", command=lambda:add_to_entry(root, "root"))
    remainder= tk.Button(root, text=u"\uFE6A", command=lambda:add_to_entry(root, "%"))
    e = tk.Button(root, text="e", command=lambda:add_to_entry(root, "e"))

    seven = tk.Button(root, text="7", command=lambda:add_to_entry(root, "7"))
    eight = tk.Button(root, text="8", command=lambda:add_to_entry(root, "8"))
    nine = tk.Button(root, text="9", command=lambda:add_to_entry(root, "9"))
    divide = tk.Button(root, text=u"\u00F7", command=lambda:add_to_entry(root, "/"))

    four = tk.Button(root, text="4", command=lambda:add_to_entry(root, "4"))
    five = tk.Button(root, text="5", command=lambda:add_to_entry(root, "5"))
    six = tk.Button(root, text="6", command=lambda:add_to_entry(root, "6"))
    multiply = tk.Button(root, text=u"\u00D7", command=lambda:add_to_entry(root, "*"))

    one = tk.Button(root, text="1", command=lambda:add_to_entry(root, "1"))
    two = tk.Button(root, text="2", command=lambda:add_to_entry(root, "2"))
    three = tk.Button(root, text="3", command=lambda:add_to_entry(root, "3"))
    subtract = tk.Button(root, text=u"\u2212", command=lambda:add_to_entry(root, "-"))

    zero = tk.Button(root, text="0", command=lambda:add_to_entry(root, "0"))
    decimal = tk.Button(root, text=".", command=lambda:add_to_entry(root, "."))
    negative = tk.Button(root, text=u"(\u2212)", command=lambda:add_to_entry(root, "-"))
    add = tk.Button(root, text="+", command=lambda:add_to_entry(root, "+"))

    go = tk.Button(root, text="=", command=lambda:execute_entry(root))

    # fill grid
    entry1_label.grid(row=0, column=0)
    entry2_label.grid(row=1, column=0)
    entry3_label.grid(row=2, column=0)
    entry4_label.grid(row=3, column=0)
    entry5_label.grid(row=4, column=0)
    entry6_label.grid(row=5, column=0)
    entry7_label.grid(row=6, column=0)

    entry1.grid(row=0, column=1, columnspan=GROUP_COLS, sticky=tk.W+tk.E)
    entry2.grid(row=1, column=1, columnspan=GROUP_COLS, sticky=tk.W+tk.E)
    entry3.grid(row=2, column=1, columnspan=GROUP_COLS, sticky=tk.W+tk.E)
    entry4.grid(row=3, column=1, columnspan=GROUP_COLS, sticky=tk.W+tk.E)
    entry5.grid(row=4, column=1, columnspan=GROUP_COLS, sticky=tk.W+tk.E)
    entry6.grid(row=5, column=1, columnspan=GROUP_COLS, sticky=tk.W+tk.E)
    entry7.grid(row=6, column=1, columnspan=GROUP_COLS, sticky=tk.W+tk.E)

    x.grid(row=8, column=1, sticky=tk.W+tk.E)
    y.grid(row=8, column=2, sticky=tk.W+tk.E)
    square.grid(row=8, column=3, sticky=tk.W+tk.E)
    power.grid(row=8, column=4, sticky=tk.W+tk.E)
                   
    open_parens.grid(row=9, column=1, sticky=tk.W+tk.E)
    close_parens.grid(row=9, column=2, sticky=tk.W+tk.E)
    less_than.grid(row=9, column=3, sticky=tk.W+tk.E)
    greater_than.grid(row=9, column=4, sticky=tk.W+tk.E)

    absolute.grid(row=10, column=1, sticky=tk.W+tk.E)
    pi.grid(row=10, column=2, sticky=tk.W+tk.E)
    less_than_equal.grid(row=10, column=3, sticky=tk.W+tk.E)
    greater_than_equal.grid(row=10, column=4, sticky=tk.W+tk.E)

    square_root.grid(row=11, column=1, sticky=tk.W+tk.E)
    n_root.grid(row=11, column=2, sticky=tk.W+tk.E)
    remainder.grid(row=11, column=3, sticky=tk.W+tk.E)
    e.grid(row=11, column=4, sticky=tk.W+tk.E)

    seven.grid(row=8, column=6, sticky=tk.W+tk.E)
    eight.grid(row=8, column=7, sticky=tk.W+tk.E)
    nine.grid(row=8, column=8, sticky=tk.W+tk.E)
    divide.grid(row=8, column=9, sticky=tk.W+tk.E)

    four.grid(row=9, column=6, sticky=tk.W+tk.E)
    five.grid(row=9, column=7, sticky=tk.W+tk.E)
    six.grid(row=9, column=8, sticky=tk.W+tk.E)
    multiply.grid(row=9, column=9, sticky=tk.W+tk.E)

    one.grid(row=10, column=6, sticky=tk.W+tk.E)
    two.grid(row=10, column=7, sticky=tk.W+tk.E)
    three.grid(row=10, column=8, sticky=tk.W+tk.E)
    subtract.grid(row=10, column=9, sticky=tk.W+tk.E)

    zero.grid(row=11, column=6, sticky=tk.W+tk.E)
    decimal.grid(row=11, column=7, sticky=tk.W+tk.E)
    negative.grid(row=11, column=8, sticky=tk.W+tk.E)
    add.grid(row=11, column=9, sticky=tk.W+tk.E)

    go.grid(row=8, column=13, columnspan=2, rowspan=4, sticky=tk.W+tk.E)


def main():
    root = tk.Tk()

    configure_grid(root)
    create_widgets(root)

    root.mainloop()

if __name__ == '__main__':
    main()
