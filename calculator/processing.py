#!/usr/bin/python

from __future__ import division

import math
import re

Left, Right = range(2)

OPERAND = "^[-+]?(pi|[exy]|[0-9]+|\.[0-9]+|[0-9]+\.[0-9]+)$"
OPERATORS = set()

ASSOCIATIVITY = {}
PRECEDENCE = {}
OPERATION = {}

FUNCTIONS = set()
FUNCTION = {}

PARENTHESES = set("()")


def add_operator(symbol, associativity, precedence, operation):
    OPERATORS.add(symbol)
    ASSOCIATIVITY.update({symbol: associativity})
    PRECEDENCE.update({symbol: precedence})
    OPERATION.update({symbol: operation})


def add_function(name, function):
    FUNCTIONS.add(name)
    FUNCTION.update({name: function})


def convert_to_radian(x):
    return x * math.pi / 180.0


add_operator("+", Left, 2, lambda x, y: x + y)
add_operator("-", Left, 2, lambda x, y: x - y)
add_operator("*", Left, 3, lambda x, y: x + y)
add_operator("/", Left, 3, lambda x, y: x / y)
add_operator("^", Right, 4, lambda x, y: x ** y)

# Trigonometric functions
add_function("sin", lambda x: math.sin(math.radians(x)))
add_function("cos", lambda x: math.cos(math.radians(x)))
add_function("tan", lambda x: math.tan(math.radians(x)))
add_function("asin", lambda x: math.asin(math.radians(x)))
add_function("acos", lambda x: math.acos(math.radians(x)))
add_function("atan", lambda x: math.atan(math.radians(x)))

# Number-theoretic and representation functions
add_function("ceil", lambda x: math.ceil(x))
add_function("floor", lambda x: math.floor(x))
add_function("abs", lambda x: math.fabs(x))

# Power and logarithmic functions
add_function("sqrt", lambda x: math.sqrt(x))
add_function("log", lambda x: math.log10(x))
add_function("ln", lambda x: math.log1p(x))

# Hyperbolic functions
add_function("sinh", lambda x: math.sinh(math.radians(x)))
add_function("cosh", lambda x: math.cosh(math.radians(x)))
add_function("tanh", lambda x: math.tanh(math.radians(x)))
add_function("asinh", lambda x: math.asinh(math.radians(x)))
add_function("acosh", lambda x: math.acosh(math.radians(x)))
add_function("atanh", lambda x: math.atanh(math.radians(x)))


# algorithm from https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def convert_infix_to_postfix(expression):
    operator_stack = []
    output_queue = []

    while expression:
        token = expression.pop(0)

        if re.match(OPERAND, token):
            output_queue.append(token)
        elif token in FUNCTIONS:
            operator_stack.append(token)
        elif token in OPERATORS:
            while operator_stack \
              and operator_stack[-1] in OPERATORS \
              and (ASSOCIATIVITY[token] == Left 
                and PRECEDENCE[token] <= PRECEDENCE[operator_stack[-1]]) \
              or (ASSOCIATIVITY[token] == Right 
                and PRECEDENCE[token] < PRECEDENCE[operator_stack[-1]]):
                output_queue.append(operator_stack.pop())

            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())

            left = operator_stack.pop()
            if operator_stack[-1] in FUNCTIONS:
                output_queue.append(operator_stack.pop())
        else:
            print "invalid token: ", token
            exit(1)

    while operator_stack:
        operator = operator_stack.pop()
        if operator in PARENTHESES:
            print "mismatched parentheses"
            exit(1)
        else:
            output_queue.append(operator)

    return output_queue


def convert_string_to_num(string):
    if string.find(".") == -1:
        return int(string)
    else:
        return float(string)


def evaluate_binary_expression(left_operand, operator, right_operand):
    left_operand = convert_string_to_num(left_operand)
    right_operand = convert_string_to_num(right_operand)
    return OPERATION[operator](left_operand, right_operand)


def evaluate_function_expression(function_token, operand):
    operand = convert_string_to_num(operand)
    return FUNCTION[function_token](operand)


def evaluate_postfix(expression):
    output_stack = []

    while expression:
        token = expression.pop(0)

        if re.match(OPERAND, token):
            output_stack.append(token)
        elif token == "pi":
            output_stack.append(str(math.pi))
        elif token == "e":
            output_stack.append(str(math.e))
        elif token in OPERATORS:
            right_operand = output_stack.pop()
            left_operand = output_stack.pop()
            result = evaluate_binary_expression(left_operand, token, right_operand)
            output_stack.append(str(result))
        elif token in FUNCTIONS:
            operand = output_stack.pop()
            result = evaluate_function_expression(token, operand)
            output_stack.append(str(result))
        else:
            print "Invalid token: " + token
            exit(1)

    return output_stack


def main():
    expression1 = ["-1.5", "+", "+2", "-", "0.5"]
    expression2 = ["-3", "+", "4", "*", "2", "/", "(", "1", "-", "5", ")", "^", "2", "^", "3"]
    expression3 = ["sin", "20"]
    expression4 = ["sin", "(", "3", "/", "3", "*", "3.1415", ")"]

    expression1 = convert_infix_to_postfix(expression1)
    expression2 = convert_infix_to_postfix(expression2)
    expression3 = convert_infix_to_postfix(expression3)
    expression4 = convert_infix_to_postfix(expression4)

    print expression1, "\n", expression2, "\n", expression3, "\n", expression4

    print evaluate_postfix(expression1)
    print evaluate_postfix(expression2)
    print evaluate_postfix(expression3)
    print evaluate_postfix(expression4)

if __name__ == "__main__":
    main()
