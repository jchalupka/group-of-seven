#!/usr/bin/python
from fractions import gcd
import math
#Reduces user entered fraction into lowest terms

def reduceToLowestTerms(numerator,denominator):
	print numerator,"/", denominator

	greatestCommon = gcd(numerator,denominator)

	numerator = numerator/greatestCommon
	denominator = denominator/greatestCommon

	if abs(denominator) < abs(numerator):
		print "you have entered a improper fraction"
		greatestCommon = math.gcd(numerator,denominator)
		numerator = numerator/greatestCommon
		denominator = denominator/greatestCommon
		resultWhole = numerator // denominator
		result = numerator % denominator
		print resultWhole, result,"/",denominator
	else:
		greatestCommon = math.gcd(numerator,denominator)

		numerator = numerator/greatestCommon
		denominator = denominator/greatestCommon

		print numerator,"/", denominator

#Quick test of the function
print "Enter the numerator"
numer = input()
print "Enter the denominator"
denom = input()
reduceToLowestTerms(numer,denom)






