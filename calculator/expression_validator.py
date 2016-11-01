#!/usr/bin/python
import re

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
def is_valid(expression):
	valid_p = valid_parentheses(expression)
	valid_a = valid_arithmetic_expression(expression)

	# if  not valid_p:	
	# 	print found_not_valid(found_missing_parenthesis)
	# if not valid_a:
	# 	print found_not_valid(found_missing_arithmetic_expression)
	# if valid_p and valid_a:
	# 	print found_valid()

	return valid_p and valid_a

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

	expression = expression.replace('-','+ -1 *')
	expression = expression.replace(' ','')
	expression = re.compile(r'(-*[A-Za-z]|-*\d+)|([\+\-\/\*\(\)])').split(expression)
	expression = filter(None, expression)


	# Now we have an expression in list form seperated into individual componenets
	# eg ['29', '**', '(', '59', '+', '4', '-', '3', ')', '/', '6']
	
	stack = expression;

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
	#print expression
	valid = is_valid(expression)
	if valid: print 'Valid'
	else: print 'Invalid'
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