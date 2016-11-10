#!/usr/bin/python

from operators import *
import re

def evaluate_postfix(expression):
    output_stack = []

    while expression:
        token = expression.pop(0)

        if re.match(operand, token):
            output_stack.append(token)
        elif token in operators:
            operand1 = output_stack.pop()
            operand2 = output_stack.pop()
            infix_expression = operand2 + token + operand1
            print infix_expression

    return output_stack

def main():
    expression1 = ['3', '4', '2', '*', '1', '5', '-', '2', '3', '^', '^', '/', '+']
    expression2 = ['3', '3', '/', '3.1415', '*', 'sin']
    expression3 = ['3', '2', '+']

    # print evaluate_postfix(expression1);
    # print evaluate_postfix(expression2);
    print evaluate_postfix(expression3);

if __name__ == "__main__":
    main()
