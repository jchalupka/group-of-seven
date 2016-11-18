#!/usr/bin/python

from __future__ import division

import math
import re

Left, Right = range(2)

OPERAND_REGEX = "[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?|pi|PI|[eExX]"
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
add_operator("/", Left, 3, lambda x, y: x / y)
add_operator("%", Left, 3, lambda x, y: x % y)
add_operator("^", Right, 4, lambda x, y: x ** y)

# Trigonometric functions
add_function("sin", lambda x: math.sin(x))
add_function("cos", lambda x: math.cos(x))
add_function("tan", lambda x: math.tan(x))
add_function("asin", lambda x: math.asin(x))
add_function("acos", lambda x: math.acos(x))
add_function("atan", lambda x: math.atan(x))

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


def find_error(expression):
    if type(expression) is str:
        return True


def variable_in_expression(expression):
    try:
        expression.index("x")
        return True
    except ValueError:
        return False


def evaluate_expression(expression, range):
    infix_expression = valid_arithmetic_expression(expression)    
    if find_error(infix_expression):
        return infix_expression
    
    postfix_expression = infix_to_postfix(infix_expression) 
    if find_error(postfix_expression):
        return postfix_expression

    if variable_in_expression(postfix_expression):
        return get_xy_values(postfix_expression, range)
    else:
        return evaluate_postfix(postfix_expression)


def matching_parentheses(expression):
    parentheses = []
    for i in expression:
        if i is '(':
            parentheses.append(i)
        elif i is ')':
            if parentheses:
                parentheses.pop()
            else:
                return False
    if parentheses:
        return False
    else:
        return True


def valid_arithmetic_expression(expression):
    if not matching_parentheses(expression):
        return "Mismatched parentheses"

    expression = to_expression_list(expression)
    expression_copy = list(expression)

    symbols = ['sin','cos','tan',
               'asin','acos','atan',
               'sinh','cosh','tanh',
               'asinh','acosh','atanh',
               'ceil','floor','abs','sqrt','log','ln',
               'pi', 'e', '!']
    symbols += ['-' + symbol for symbol in symbols]

    stack = expression;
    for token in expression:
        if token in symbols:
            loc = expression.index(token)
            if token == '!':
                expression[loc] = '*'
                expression.insert(loc + 1, '1')
            
            elif re.match('-*(pi|e)', token):
                expression[loc] = '1'
            else:
                if expression[loc][0] == '-':
                    expression[loc] = '-1'
                else:
                    expression[loc] = '1'
                expression.insert(loc + 1, '*')


    # State 0 can accept number, letter or (
    # State 1 can accept operation or )

    state = 0

    if not stack:
        return "Invalid expression"

    # Check for corner case with one variable
    # if (re.match('-*[xX]', stack[0]) and len(stack) == 1):
    #     return False

    while stack:
        token = stack.pop(0)
        if state is 0:
            if re.match('^-*x|-*\.[0-9]+|-*[0-9]+\.[0-9]+|-*[0-9]+$',token):
                state = 1

            elif re.match('^\($', token):
                state = 0
            else:
                return "Invalid expression"
        elif state is 1:
            if '-' is token[0]:
                if token[1:] is not '':
                    stack.insert(0, token[1:])
                token = '-'

            if re.match('^[\+\-\/\*\^]$',token):
                state = 0
            elif re.match('^\)$',token):
                state = 1
            else:
                return "Invalid expression"

    # At the end of validation state = 1 if valid
    if state is 1:
        return expression_copy
    else:
        return "Invalid expression"


def to_expression_list(expression):
    expression = expression.lower()
    expression = expression.replace(' ','')
    expression = re.compile(r'(-*[a-z]+)|(-*\.[0-9]+|-*[0-9]+\.[0-9]+|-*[0-9]+)|([\+\-\/\*\(\)])').split(expression)

    # wont this remove zeros
    expression = filter(None, expression)

    # Test is the function begins with y = just take it out
    if re.match('[yY]\s*=.*', ''.join(expression[0:2])):
        if (expression[1].split('=')[1] != ''):
            expression.insert(2,expression[1].split('=')[1])
        expression = expression[2:]
    return expression


def ordered_by_precedence(operator_stack, token):
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
              and ordered_by_precedence(operator_stack, token):
                output_queue.append(operator_stack.pop())

            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())

            left = operator_stack.pop()
            if operator_stack and operator_stack[-1] in FUNCTIONS:
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


def get_xy_values(postfix_expression, max):
    xy_values = []

    min = max * -1
    step = (max - min) / 32

    x_indices = [j for j, k in enumerate(postfix_expression) if k == "x"]

    x = y = min

    while x <= max:
        expression_copy = list(postfix_expression)

        for x_index in x_indices:
            expression_copy[x_index] = str(x)

        try:
            y = evaluate_postfix(expression_copy)
            y = float(y)
            if y >= min and y <= max:
                xy_values.append(tuple((x, y)))
        except ValueError:
            return y

        x += step

    print xy_values
    return xy_values


def string_to_num(string):
    if string == "pi":
        return math.pi
    elif string == "e":
        return math.e
    elif string.find(".") != -1:
        return float(string)
    else:
        return int(string)


def evaluate_binary_expression(left_operand, operator, right_operand):
    try:
        left_operand = string_to_num(left_operand)
        right_operand = string_to_num(right_operand)
        return OPERATION[operator](left_operand, right_operand)
    except ValueError:
        return "Domain error"
    except ZeroDivisionError:
        return "Divide by zero error"
    except OverflowError:
        return "Out of range"

def evaluate_unary_expression(function_token, operand):
    operand = string_to_num(operand)

    try:
        if function_token in FUNCTIONS:
            return FUNCTION[function_token](operand)
        else:
            return OPERATION[operator](operand)
    except ValueError:
        return "Domain error"
    except ZeroDivisionError:
        return "Divide by zero error"
    except OverflowError:
        return "Out of range"

def evaluate_postfix(expression):
    output_stack = []

    while expression:
        token = expression.pop(0)

        if re.match(OPERAND_REGEX, token):
            output_stack.append(token)
        elif token == "pi":
            output_stack.append("pi")
        elif token == "e":
            output_stack.append("e")
        elif token == "!":
            operand = output_stack.pop()
            result = evaluate_unary_expression(token, operand)
            output_stack.append(str(result))
        elif token in OPERATORS:
            right = output_stack.pop()
            left = output_stack.pop()
            result = evaluate_binary_expression(left, token, right)
            output_stack.append(str(result))
        elif token in FUNCTIONS:
            operand = output_stack.pop()
            result = evaluate_unary_expression(token, operand)
            output_stack.append(str(result))
        else:
            return "Invalid token"
            
    return output_stack.pop()
