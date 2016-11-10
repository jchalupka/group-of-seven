#!/usr/bin/python

Left, Right = range(2)

operand = "^-?([xy]|[0-9]+|\.[0-9]+|[0-9]+\.[0-9]+)$"
operators = set() 
associativity = {}
precedence = {}

functions = set("sin cos tan log sec csc cot abs exp mod ceil floor ln".split())
parentheses = set("()")

def add_operator(operator_symbol, operator_associativity, operator_precedence):
    operators.add(operator_symbol)
    associativity.update({operator_symbol: operator_associativity})
    precedence.update({operator_symbol: operator_precedence})

add_operator("+", Left, 2)
add_operator("-", Left, 2)
add_operator("*", Left, 3)
add_operator("/", Left, 3)
add_operator("^", Right, 4)

