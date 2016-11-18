#!/usr/bin/env python

import app.calculator.processing as pro
import unittest


class TestProcessing(unittest.TestCase):

    def test_evaluate_expression(self):
        self.assertEqual(pro.evaluate_expression("4", 10), "4")
        # self.assertEqual(pro.evaluate_expression("1-2", 10), "-1")
        self.assertEqual(pro.evaluate_expression("2 * 2 + 3", 10), "7")
        self.assertEqual(pro.evaluate_expression("(2 * 2) + 3", 10), "7")
        self.assertEqual(pro.evaluate_expression("2/1 * (3 * -4)", 10), "-24.0")
        self.assertEqual(pro.evaluate_expression("2/1 * (3 * -4)", 10), "-24.0")
        # self.assertEqual(pro.evaluate_expression("y = x/2", 10), [])
        # self.assertEqual(pro.evaluate_expression("y = (x/3 + x)", 20), [])
        # self.assertEqual(pro.evaluate_expression("y = (  (x + 4) * 2 - 3  )", 40), [])
        # self.assertEqual(pro.evaluate_expression("y = (x-x)/(2+60*x)-( x*100)", 80), [])
        # self.assertEqual(pro.evaluate_expression("y = sin(x)", 160), [])
        # self.assertEqual(pro.evaluate_expression("sin(x)", 200), [])
        # self.assertEqual(pro.evaluate_expression("tan(x)", 700), [])
        # self.assertEqual(pro.evaluate_expression("y = 2 * (sin(x) + 2/5) - tan(7000)", 800), [])
        # self.assertEqual(pro.evaluate_expression("2.5 * 9.001, 10"), [])
        self.assertEqual(pro.evaluate_expression("y = helloWorld", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("20x", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("4 y", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("x+ ", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("+123", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("( x + y", 10), "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(m + n", 10), "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("xy)", 10), "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(y 10)", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("(x - 61) - (2-400))", 10), "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(a-b/(x*y)", 10), "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(a+b)/((c-100)20", 10), "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(i- j)(t+k )", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y=", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y=y", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("a+1", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y = a + b", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y = y + 2", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y", 10), "Invalid expression")
        self.assertEqual(pro.evaluate_expression("s", 10), "Invalid expression")
        # self.assertEqual(pro.evaluate_expression("x + x", 10), [])
        # self.assertEqual(pro.evaluate_expression("y = x+x", 10), [])
        # self.assertEqual(pro.evaluate_expression("y = x/2", 10), [])

    def test_infix_to_postfix(self):
        self.assertEqual(pro.infix_to_postfix(
            ["1", "+", "2"]), ["1", "2", "+"])

        self.assertEqual(pro.infix_to_postfix(
            ["1.0", "-", "2.5"]), ["1.0", "2.5", "-"])

        self.assertEqual(pro.infix_to_postfix(
            ["1", "*", "2"]), ["1", "2", "*"])

        self.assertEqual(pro.infix_to_postfix(
            ["1", "/", "2"]), ["1", "2", "/"])

        self.assertEqual(pro.infix_to_postfix(
            ["1", "^", "2"]), ["1", "2", "^"])

        self.assertEqual(pro.infix_to_postfix(
            ["sin", "20"]), ["20", "sin"])

    def test_evaluate_postfix(self):
        self.assertEqual(pro.evaluate_postfix(["1", "2", "+"]), "3")
        self.assertEqual(pro.evaluate_postfix(["1.0", "2.5", "-"]), "-1.5")
        self.assertEqual(pro.evaluate_postfix(["1", "2", "*"]), "2")
        self.assertEqual(pro.evaluate_postfix(["1", "2", "/"]), "0.5")
        self.assertEqual(pro.evaluate_postfix(["pi", "6", "*"]), "18.8495559215")
        self.assertEqual(pro.evaluate_postfix(["7.25", "floor"]), "7.0")
        self.assertEqual(pro.evaluate_postfix(["7.25", "ceil"]), "8.0")
        self.assertEqual(pro.evaluate_postfix(["20", "cos"]), "0.408082061813")
        self.assertEqual(pro.evaluate_postfix(["20", "tan"]), "2.23716094422")
        self.assertEqual(pro.evaluate_postfix(["1", "0", "/"]), "Divide by zero error")
        self.assertEqual(pro.evaluate_postfix(["1", "asin"]), "1.57079632679")
        self.assertEqual(pro.evaluate_postfix(["10", "asin"]), "Domain error")
        self.assertEqual(pro.evaluate_postfix(["-1", "acos"]), "3.14159265359")
        self.assertEqual(pro.evaluate_postfix(["10", "acos"]), "Domain error")
        self.assertEqual(pro.evaluate_postfix(["-1", "atan"]), "-0.785398163397")
        self.assertEqual(pro.evaluate_postfix(["3", "sinh"]), "10.0178749274")
        self.assertEqual(pro.evaluate_postfix(["3", "cosh"]), "10.0676619958")
        self.assertEqual(pro.evaluate_postfix(["3000", "cosh"]), "Out of range")
        self.assertEqual(pro.evaluate_postfix(["3", "tanh"]), "0.995054753687")
        self.assertEqual(pro.evaluate_postfix(["0.5", "asinh"]), "0.48121182506")
        self.assertEqual(pro.evaluate_postfix(["1.4", "acosh"]), "0.867014726491")
        self.assertEqual(pro.evaluate_postfix(["-1", "acosh"]), "Domain error")
        self.assertEqual(pro.evaluate_postfix(["0.5", "atanh"]), "0.549306144334")

    def test_string_to_num(self):
        self.assertEqual(pro.string_to_num("1"), 1)
        self.assertEqual(pro.string_to_num("1.0"), 1.0)

    def test_evaluate_binary_expression(self):
        self.assertEqual(pro.evaluate_binary_expression("1", "/", "2"), 0.5)
        self.assertEqual(pro.evaluate_binary_expression("1", "*", "2"), 2)

    def test_evaluate_unary_expression(self):
        self.assertEqual(pro.evaluate_unary_expression("sinh", "2.5"), 6.0502044810397875)

        self.assertEqual(pro.evaluate_unary_expression("floor", "2.2"), 2.0)
        self.assertEqual(pro.evaluate_unary_expression("ceil", "2.2"), 3.0)
        self.assertEqual(pro.evaluate_unary_expression("abs", "-2"), 2)

        self.assertEqual(pro.evaluate_unary_expression("sqrt", "2"), 1.4142135623730951)
        self.assertEqual(pro.evaluate_unary_expression("log", "10"), 1)
        self.assertEqual(pro.evaluate_unary_expression("ln", "10"), 2.3978952727983707)

    def is_valid(self, expression):
        valid_a = pro.valid_arithmatic_expression(expression)
        valid_p = pro.valid_arithmatic_expression(expression)

        if not (valid_a and valid_p):
            return False
        return True


    def test_validator(self):
        # VALID TESTS
        self.assertTrue(is_valid('4'))
        self.assertTrue(is_valid('1-2'))
        self.assertTrue(is_valid('2 * 2 + 3'))
        self.assertTrue(is_valid('(2 * 2) + 3'))
        self.assertTrue(is_valid('2/1 * (3 * -4)'))
        self.assertTrue(is_valid('x + x'))
        self.assertTrue(is_valid('y = x+x'))
        self.assertTrue(is_valid('y = x/2'))
        self.assertTrue(is_valid('y = (x/3 + x)'))
        self.assertTrue(is_valid('y = (  (x + 4) * 2 - 3  )'))
        self.assertTrue(is_valid('y = (x-x)/(2+60*x)-( x*100)'))
        self.assertTrue(is_valid('y = sin(x)'))
        self.assertTrue(is_valid('sin(x)'))
        self.assertTrue(is_valid('tan(x)'))
        self.assertTrue(is_valid('y = 2 * (sin(x) + 2/5) - tan(7000)'))
        self.assertTrue(is_valid('2.5 * 9.001'))
        self.assertTrue(is_valid('y=x'))
        self.assertTrue(is_valid('y=1'))
        self.assertTrue(is_valid('y = 2+2'))
        self.assertTrue(is_valid('y = 2+ x'))
        self.assertTrue(is_valid('pi'))
        self.assertTrue(is_valid('y = pi'))
        self.assertTrue(is_valid('2 * -pi'))
        self.assertTrue(is_valid('pi * pi'))
        self.assertTrue(is_valid(' y = pi'))
        self.assertTrue(is_valid('sin(20 * 16 - 5)/2'))
        self.assertTrue(is_valid('sin(20^5)'))
        self.assertTrue(is_valid('sin(cos(tan 50))'))
        self.assertTrue(is_valid('5!'))
        self.assertTrue(is_valid('1-2'))
        
        #INVALID TESTS
        self.assertFalse(is_valid('y = helloWorld'))
        self.assertFalse(is_valid('20x'))
        self.assertFalse(is_valid('4 y'))
        self.assertFalse(is_valid('x+ '))
        self.assertFalse(is_valid('+123'))
        self.assertFalse(is_valid('( x + y'))
        self.assertFalse(is_valid('(m + n'))
        self.assertFalse(is_valid('xy)'))
        self.assertFalse(is_valid('(y 10)'))
        self.assertFalse(is_valid('(x - 61) - (2-400))'))
        self.assertFalse(is_valid('(a-b/(x*y)'))
        self.assertFalse(is_valid('(a+b)/((c-100)20'))
        self.assertFalse(is_valid('(i- j)(t+k )'))
        self.assertFalse(is_valid('y='))
        self.assertFalse(is_valid('y=y'))
        self.assertFalse(is_valid('a+1'))
        self.assertFalse(is_valid('y = a + b'))
        self.assertFalse(is_valid('y = y + 2'))
        self.assertFalse(is_valid(''))
        self.assertFalse(is_valid('y'))
        self.assertFalse(is_valid('s'))
        self.assertFalse(is_valid('helloWorld'))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProcessing)
    unittest.TextTestRunner(verbosity=2).run(suite)
