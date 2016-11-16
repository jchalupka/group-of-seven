#!/usr/bin/python
import re
import calculator_gui
import processing

# Jordan Chalupka
# CIS*3250

# Validation of an arithmetic expression
# This module takes an arithmatic expression as input and 
#   returns if the expression is a valid arithmatic expression.

#  Updated to now check for functions, and defined symbols

def gui_function_validator(expression, status_root):
    valid_p = valid_parentheses(expression)
    valid_a = valid_arithmetic_expression(expression)

    answer = None

    if not (valid_p and valid_a):
        calculator_gui.update_status(status_root, result_message(valid_p, valid_a))
        return None
    else:
        calculator_gui.update_status(status_root, '')
        print 'I\'m going to call Shuntingyard'
        term_list = to_expression_list(expression)
        print term_list
        
        result = processing.infix_to_postfix(term_list)
        print result

        answer = processing.evaluate_postfix(result)
        answer = answer[0]


        # Call Shuntingyard here
  
    return answer


def result_message(valid_p, valid_a):
        if not (valid_p and valid_a):
            if not valid_p:
                return 'An invalid arithmetic expression:  mismatch parentheses'
            else:
                return 'An invalid arithmetic expression:  missing arithmetic operators/operands'

        else:
            return 'A valid arithmetic expression'


#
# Returns a boolean represening if the parenthesis are valid
#
def valid_parentheses(expression):
    stack = list()
    for x in expression:
        if x is '(': stack.append(x) 
        elif x is ')': 
            if len(stack): stack.pop() 
            else: return False
    return True if len(stack) is 0 else False 

#
# Returns a boolean representing if the arithmatic operators are valid
#
def valid_arithmetic_expression(expression):
    expression = to_expression_list(expression)

    # Now we have an expression in list form seperated into individual componenets
    # eg ['29', '**', '(', '59', '+', '4', '-', '3', ')', '/', '6']
    
    symbols = ['sin','cos','tan',
               'asin','acos','atan',
               'sinh','cosh','tanh',
               'asinh','acosh','atanh',
               'ceil','floor','abs','sqrt','log','ln',
               'pi', 'e']
    symbols += ['-' + symbol for symbol in symbols]

    stack = expression;
    #print stack
    for token in expression:
        if token in symbols:
            loc = expression.index(token)
            if re.match('-*(pi|e)', token):
                expression[loc] = '1'
            elif expression[loc+1] is '(' and  re.match('-*\.[0-9]+|-*[0-9]+\.[0-9]+|-*[0-9]+|-*x',expression[loc+2]) and expression[loc+3] is ')':
                if expression[loc][0] == '-':
                    expression[loc] = '-1'
                else:
                    expression[loc] = '1'
                expression.pop(loc+1)
                expression.pop(loc+1)
                expression.pop(loc+1)

    #print stack

    # State 0 can accept number, letter or (
    # State 1 can accept operation or )
    
    state = 0 


    if (len(stack) == 0):
        return False

    # Check for corner case with one variable
    # if (re.match('-*[xX]', stack[0]) and len(stack) == 1):
    #     return False

    # Test is the function begins with y = just take it out 
    if re.match('[yY]\s*=.*', ''.join(stack[0:2])):   
        if (stack[1].split('=')[1] != ''): 
            stack.insert(2,stack[1].split('=')[1])
        stack = stack[2:]

    while len(stack) > 0:
        token = stack.pop(0)
        if state is 0:
            if re.match('^-*x|-*\.[0-9]+|-*[0-9]+\.[0-9]+|-*[0-9]+$',token):
                state = 1

            elif re.match('^\($', token):
                state = 0
            else: 
                return False
        elif state is 1:
            if '-' is token[0]:
                if token[1:] is not '':
                    stack.insert(0, token[1:])
                token = '-'

            if re.match('^[\+\-\/\*]$',token):
                state = 0
            elif re.match('^\)$',token):
                state = 1
            else: 
                return False
    # At the end of validation state = 1 if valid
    if state is 1: return True 
    else: return False

#
# Change to list
#
def to_expression_list(expression):
    #expression = expression.replace('-','+ -1 *')
    expression = expression.lower()
    expression = expression.replace(' ','')
    expression = re.compile(r'(-*[a-z]+)|(-*\.[0-9]+|-*[0-9]+\.[0-9]+|-*[0-9]+)|([\+\-\/\*\(\)])').split(expression)

    expression = filter(None, expression)

    # Test is the function begins with y = just take it out 
    if re.match('[yY]\s*=.*', ''.join(expression[0:2])):   
        if (expression[1].split('=')[1] != ''): 
            expression.insert(2,expression[1].split('=')[1])
        expression = expression[2:]
    return expression


#
# Start of responses
#
def found_valid():
    return "A valid arithmetic expression"

def found_not_valid(reason):
    return "An invalid arithmetic expression: " + reason() 

def found_missing_parenthesis():
    return "mismatch parentheses"

def found_missing_arithmetic_expression():
    return "missing arithmetic operators/operands"
# End of responses

#
# Some tests
#
def test(expression):
    valid_p = valid_parentheses(expression)
    valid_a = valid_arithmetic_expression(expression)
    if valid_p and valid_a: print 'Valid'
    else: print 'Invalid'

    #print result_message(valid_p,valid_a)
    return valid_p and valid_a

def run_valid_tests():
    correct = 0
    print 'VALID TESTS'
    if test('4'): correct += 1
    if test('1-2'): correct  += 1 
    if test('2 * 2 + 3'): correct += 1
    if test('(2 * 2) + 3'): correct += 1
    if test('2/1 * (3 * -4)'): correct += 1
    if test('x + x'): correct += 1
    if test('y = x+x'): correct += 1
    if test('y = x/2'): correct  += 1
    if test('y = (x/3 + x)'): correct  += 1
    if test('y = (  (x + 4) * 2 - 3  )'): correct  += 1
    if test('y = (x-x)/(2+60*x)-( x*100)'): correct  += 1
    if test('y = sin(x)'): correct += 1
    if test('sin(x)'): correct += 1
    if test('tan(x)'): correct += 1
    if test('y = 2 * (sin(x) + 2/5) - tan(7000)'): correct += 1
    if test('2.5 * 9.001'): correct += 1

    if test('y=x'): correct += 1
    if test('y=1'): correct += 1
    if test('y = 2+2'): correct +=1
    if test('y = 2+ x'): correct +=1
    if test('pi'): correct += 1
    if test('y = pi'): correct += 1
    if test('2 * -pi'): correct += 1
    if test('pi * pi'): correct += 1
    if test(' y = pi'): correct += 1

    print 'END OF VALID TESTS'
    print correct,'/ 25 Correct.'

def run_invalid_tests():
    correct = 0
    print 'INVALID TESTS'
    if not test('y = helloWorld'): correct += 1
    if not test('20x'): correct += 1
    if not test('4 y'): correct += 1
    if not test('x+ '): correct += 1
    if not test('+123'): correct += 1
    if not test('( x + y'): correct += 1
    if not test('(m + n'): correct += 1
    if not test('xy)'): correct += 1
    if not test('(y 10)'): correct += 1
    if not test('(x - 61) - (2-400))'): correct += 1
    if not test('(a-b/(x*y)'): correct += 1
    if not test('(a+b)/((c-100)20'): correct += 1
    if not test('(i- j)(t+k )'): correct += 1

    if not test('y='): correct += 1
    if not test('y=y'): correct += 1
    if not test('a+1'): correct += 1
    if not test('y = a + b'): correct += 1
    if not test('y = y + 2'): correct += 1
    if not test(''): correct += 1
    if not test('y'): correct += 1
    if not test('s'): correct += 1
    if not test('helloWorld'): correct += 1
    print 'END OF INVALID TESTS'
    print correct,'/ 22 Correct.'
# End of tests

def main():
    # Test cases
    # Valid
    run_valid_tests()

    #Invalid
    run_invalid_tests()
    

if __name__ == '__main__':
    main()

#EOF