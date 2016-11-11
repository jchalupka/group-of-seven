#!/usr/bin/env python

import re
import calculator_gui

# Jordan Chalupka
# CIS*3250

# Validation of an arithmetic expression
# This module takes an arithmatic expression as input and
#	returns if the expression is a valid arithmatic expression.

# Things to check:
#   -missing parenthesis eg. 2 + (5 - 7
#   -missing arithmetic operators/operands eg. 99 * 42 */3

#
# Returns a boolean value representing the validity of the expression
# Prints out a message as a side effect
#
def is_valid(expression, status_root, type):
    response = found_valid(type)
    if type == "Calculation":
        valid_a = valid_arithmetic_expression(expression)
        if not valid_a:
        	    response = found_not_valid(found_missing_arithmetic_expression)
    elif type == "Graph":
        valid_a = valid_graphing_expression(expression)
        if not valid_a:
    	    response = found_not_valid(found_missing_graphing_expression)
    valid_p = valid_parentheses(expression)
    if not valid_p:
    	 response = found_not_valid(found_missing_parenthesis)
    calculator_gui.update_status(status_root, response)
    #print "paratheses: " + str(valid_p)
    #print "cal: " + str(valid_a)
    return valid_p and valid_a

#
# Returns a boolean represening if the parenthesis are valid
#
def valid_parentheses(expression):
    stack = list()
    print expression
    for x in expression:
        if x is '(':
            stack.append(x)
        elif x is ')':
            if len(stack): stack.pop()
            else: return False
    return True if len(stack) is 0 else False

#
# Returns the expression spereated into individual components as a list
#
def seperate(expression):
	expression = expression.replace('-','+ -1 *')
	expression = expression.replace(' ','')
	expression = re.compile(r'(-*[A-Za-z]|-*\d+)|([\+\-\/\*\(\)\^])').split(expression)
	expression = filter(None, expression)
	return expression

#
# Returns a boolean representing if the arithmatic operators are valid
#
def valid_arithmetic_expression(expression):
    stack = seperate(expression)
	# State 0 can accept number, letter or (
	# State 1 can accept operation or )
    state = 0
    while len(stack) > 0:
        token = stack.pop(0)
        if state is 0:
			if re.match('^-*[A-Za-z]|-*\d+$',token):
				state = 1

			elif re.match('^\($', token):
				state = 0
			else:
				return False
        elif state is 1:
			if re.match('^[\+\-\/\*\^]$',token):
				state = 0
			elif re.match('^\)$',token):
				state = 1
			else:
				return False
	# At the end of validation state = 1 if valid
    if state is 1: return True
    else: return False

def valid_graphing_expression(expression):
    stack = seperate(expression)
    # State 0 can accept number, letter or (
    # State 1 can accept operation or )
    state = 0
    x = 0
    while len(stack) > 0:
        token = stack.pop(0)

        if state is 0:
            if re.match('^-*[xX]|-*\d+$',token):
                state = 1
                if token == "x":
                    x += 1
            elif re.match('^\($', token):
                state = 0
            else:
                return False
        elif state is 1:
            if re.match('^[\+\-\/\*\^]$',token):
                state = 0
            elif re.match('^\)$',token):
                state = 1
            else:
                return False
    # At the end of validation state = 1 if valid
    if state is 1 | x != 0: return True
    else: return False

#
# Start of responses
#
def found_valid(type):
	return "*" + type + " successfully processed"

def valid_graph(expression):
    return "*Now graphing: " + expression

def Invalid_graph(reason):
    return "*Invalid graphical expression: " + reason()

def found_not_valid(reason):
	return "*An invalid arithmetic expression: " + reason()

def found_missing_parenthesis():
	return "*Mismatch parentheses"

def found_missing_arithmetic_expression():
	return "*Missing arithmetic operators/operands"

def found_missing_graphing_expression():
    return "*Missing variable x or arithmetic operators/operands"
# End of responses

#
# Some tests
#
def test(expression, status_root, type):
	#print expression
	valid = is_valid(expression, status_root, type)
	#if valid: print 'Valid'
	#else: print 'Invalid'
	return valid

def run_valid_tests():
	correct = 0
	print 'VALID TESTS'
	if test('a+b'): correct += 1
	if test('1-2'): correct  += 1
	if test('x/2'): correct  += 1
	if test('(a/3 + c)'): correct  += 1
	if test('(  (a + 4) * 2 - 3  )'): correct  += 1
	if test('(x-z)/(2+60*n)-( q*100)'): correct  += 1
	print 'END OF VALID TESTS'
	print correct,'/ 6 Correct.'

def run_invalid_tests():
	correct = 0
	print 'INVALID TESTS'
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
	print 'END OF INVALID TESTS'
	print correct,'/ 12 Correct.'
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
