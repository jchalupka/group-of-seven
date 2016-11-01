#!/usr/bin/python

import re

# algorithm from https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def convert_infix_to_postfix(expression):
    Left, Right = range(2)

    associativity = {"+": Left, "-": Left, "*": Left, "/": Left, "^": Right}
    precedence = {"+": 2, "-": 2, "*": 3, "/": 3, "^": 4}
    operators = set("+-*/^") 
    functions = set("sin cos".split())
    parentheses = set("()")

    operator_stack = []
    output_queue = []

    while expression:
        token = expression.pop(0)

        # match variable, integer, or floating point number
        if re.match("^[xy]|[0-9]+|\.[0-9]+|[0-9]+\.[0-9]+$", token):
            output_queue.append(token)
        elif token in functions:
            operator_stack.append(token)
        elif token in operators:
            while operator_stack and operator_stack[-1] in operators and (associativity[token] == Left and precedence[token] <= precedence[operator_stack[-1]]) or (associativity[token] == Right and precedence[token] < precedence[operator_stack[-1]]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())

            left = operator_stack.pop()
            if operator_stack[-1] in functions:
                output_queue.append(operator_stack.pop())

    while operator_stack:
        operator = operator_stack.pop()
        if operator in parentheses:
            print "mismatched parentheses"
            exit(1)
        else:
            output_queue.append(operator)

    print "operator stack: ", operator_stack
    return output_queue


def main():
    expression1 = ["3", "+", "4", "*", "2", "/", "(", "1", "-", "5", ")", "^", "2", "^", "3"]
    expression2 = ["sin", "(", "3", "/", "3", "*", "3.1415", ")"]

    postfix_expression = convert_infix_to_postfix(expression2)
    print postfix_expression

if __name__ == "__main__":
    main()
