#!/usr/bin/python

from __future__ import division

import math
import re

Left, Right = range(2)

OPERAND_REGEX = "^[-]?(pi|[exy]|[0-9]+|\.[0-9]+|[0-9]+\.[0-9]+)$"
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


add_operator("+", Left, 2, lambda x, y: x + y)
add_operator("-", Left, 2, lambda x, y: x - y)
add_operator("*", Left, 3, lambda x, y: x * y)
add_operator("/", Left, 3, lambda x, y: divide(x, y))
add_operator("^", Right, 4, lambda x, y: x ** y)

# Trigonometric functions
add_function("sin", lambda x: math.sin(math.radians(x)))
add_function("cos", lambda x: math.cos(math.radians(x)))
add_function("tan", lambda x: math.tan(math.radians(x)))
add_function("asin", lambda x: math.asin(math.radians(x)))
add_function("acos", lambda x: math.acos(math.radians(x)))
add_function("atan", lambda x: math.atan(math.radians(x)))

# Hyperbolic functions
add_function("sinh", lambda x: math.sinh(x))
add_function("cosh", lambda x: math.cosh(x))
add_function("tanh", lambda x: math.tanh(x))
add_function("asinh", lambda x: math.asinh(x))
add_function("acosh", lambda x: math.acosh(x))
add_function("atanh", lambda x: math.atanh(x))

# Number-theoretic and representation functions
add_function("ceil", lambda x: math.ceil(x))
add_function("floor", lambda x: math.floor(x))
add_function("abs", lambda x: math.fabs(x))
add_function("!", lambda x: math.factorial(x))

# Power and logarithmic functions
add_function("sqrt", lambda x: math.sqrt(x))
add_function("log", lambda x: math.log10(x))
add_function("ln", lambda x: math.log1p(x))


Min, Max = range(2)


# def evaluate_expression(expression, range):
#     validated_expression = validate_expression(expression)
#     if validated_expression in err.ERROR_MESSAGES:
#         return validated_expression
#     else:
#         postfix_expression = infix_to_postfix(validated_expression)
#         if "x" in postfix_expression:
#             xy_values = get_xy_values(expression, range)
#             # draw_graph(xy_values)


def maintain_precedence(operator_stack):
    return (ASSOCIATIVITY[token] == Left and
            PRECEDENCE[token] <= PRECEDENCE[operator_stack[-1]]) \
        or (ASSOCIATIVITY[token] == Right and
            PRECEDENCE[token] < PRECEDENCE[operator_stack[-1]])


# algorithm from https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def infix_to_postfix(expression):
    operator_stack = []
    output_queue = []

    while expression:
        token = expression.pop(0)

        if re.match(OPERAND_REGEX, token):
            output_queue.append(token)
        elif token in FUNCTIONS:
            operator_stack.append(token)
        elif token in OPERATORS:
            while operator_stack \
              and operator_stack[-1] in OPERATORS \
              and maintain_precedence(operator_stack):
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
            return "Invalid token"

    while operator_stack:
        operator = operator_stack.pop()
        if operator in PARENTHESES:
            return "Mismatched parentheses"
        else:
            output_queue.append(operator)

    return output_queue


def get_xy_values(postfix_expression, range):
    xy_values = []

    for i in range(range):
        for token in postfix_expression:
            token.replace("x", i)
        xy_values.add((i, evaluate_postfix(postfix_expression)))    

    return xy_values


def string_to_num(string):
    if string.find(".") != -1:
        return float(string)
    else:
        return int(string)


def divide(dividend, divisor):
    if divisor == 0:
        return "Divide by zero"
    else:
        return dividend / divisor


def evaluate_binary_expression(left_operand, operator, right_operand):
    left_operand = string_to_num(left_operand)
    right_operand = string_to_num(right_operand)
    return OPERATION[operator](left_operand, right_operand)


def evaluate_function_expression(function_token, operand):
    operand = string_to_num(operand)
    return FUNCTION[function_token](operand)


def evaluate_postfix(expression):
    output_stack = []

    while expression:
        token = expression.pop(0)

        if re.match(OPERAND_REGEX, token):
            output_stack.append(token)
        elif token == "pi":
            output_stack.append(str(math.pi))
        elif token == "e":
            output_stack.append(str(math.e))
        elif token in OPERATORS:
            right = output_stack.pop()
            left = output_stack.pop()
            result = evaluate_binary_expression(left, token, right)
            output_stack.append(str(result))
        elif token in FUNCTIONS:
            operand = output_stack.pop()
            result = evaluate_function_expression(token, operand)
            output_stack.append(str(result))
        else:
            return "Invalid token"

    return output_stack.pop()

