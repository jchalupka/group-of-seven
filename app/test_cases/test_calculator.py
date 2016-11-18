#!/usr/bin/env python

import app.calculator.processing as pro
import unittest


class TestProcessing(unittest.TestCase):

    def test_find_error(self):
        self.assertTrue(pro.find_error("Error message"))
        self.assertFalse(pro.find_error(1))
        self.assertFalse(pro.find_error([1, 2]))

    def test_variable_in_expression(self):
        self.assertTrue(pro.variable_in_expression(["x", "1", "2"]))
        self.assertTrue(pro.variable_in_expression(["3", "1", "x"]))
        self.assertFalse(pro.variable_in_expression(["3", "1", "4"]))

    def test_evaluate_expression(self):
        self.assertEqual(pro.evaluate_expression("4", 10), "4")
        self.assertEqual(pro.evaluate_expression("1-2", 10), "-1")
        self.assertEqual(pro.evaluate_expression("1-2-", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("2 * 2 + 3", 10), "7")
        self.assertEqual(pro.evaluate_expression("(2 * 2) + 3", 10), "7")
        self.assertEqual(pro.evaluate_expression("2/1 * (3 * -4)", 10),
                         "-24.0")
        self.assertEqual(pro.evaluate_expression("2/1 * (3 * -4)", 10),
                         "-24.0")
        self.assertEqual(pro.evaluate_expression("y = helloWorld", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("20x", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("4 y", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("x+ ", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("+123", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("( x + y", 10),
                         "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(m + n", 10),
                         "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("xy)", 10),
                         "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(y 10)", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("(x - 61) - (2-400))", 10),
                         "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(a-b/(x*y)", 10),
                         "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(a+b)/((c-100)20", 10),
                         "Mismatched parentheses")
        self.assertEqual(pro.evaluate_expression("(i- j)(t+k )", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y=", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y=y", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y=1 + 2", 10), "3")
        self.assertEqual(pro.evaluate_expression("a+1", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y = a + b", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y = y + 2", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("y", 10),
                         "Invalid expression")
        self.assertEqual(pro.evaluate_expression("s", 10),
                         "Invalid expression")

    def test_matching_parentheses(self):
        self.assertTrue(pro.matching_parentheses("y = (x-x)/(2+60*x)-( x*1)"))
        self.assertTrue(pro.matching_parentheses("y = (  (x + 4) * 2 - 3  )"))
        self.assertFalse(pro.matching_parentheses("y = (x-x)/(2+60*x)-( x*1"))

    def test_valid_arithmetic_expression(self):
        self.assertEqual(pro.valid_arithmetic_expression("x * x"),
                         ["x", "*", "x"])
        self.assertEqual(pro.valid_arithmetic_expression("y =x+ x"),
                         ["x", "+", "x"])
        self.assertEqual(pro.valid_arithmetic_expression("y = x/2"),
                         ["x", "/", "2"])
        self.assertEqual(pro.valid_arithmetic_expression("y = x/2"),
                         ["x", "/", "2"])
        self.assertEqual(pro.valid_arithmetic_expression("y = (x/3 + x)"),
                         ["(", "x", "/", "3", "+", "x", ")"])
        self.assertEqual(pro.valid_arithmetic_expression("y = sin(x)"),
                         ["sin", "(", "x", ")"])

    def test_fix_negatives(self):
        self.assertEqual(pro.fix_negatives(["-", "3"]), ["neg", "3"])
        self.assertEqual(pro.fix_negatives(["1", "-", "3"]), ["1", "-", "3"])
        self.assertEqual(pro.fix_negatives(["-", "sin", "(", "5", ")"]),
                         ["neg", "sin", "(", "5", ")"])
        self.assertEqual(pro.fix_negatives(["-", "(", "-", "3", ")"]),
                         ["neg", "(", "neg", "3", ")"])
        self.assertEqual(pro.fix_negatives(["-", "-", "3"]), ["3"])
        self.assertEqual(pro.fix_negatives(["-", "-", "-", "3"]), ["neg", "3"])

    def test_remove_y(self):
        self.assertEqual(pro.remove_y(["y", "=", "sin", "(", "x", ")"]),
                         ["sin", "(", "x", ")"])
        self.assertEqual(pro.remove_y(["y", "=", "sin", "(", "x", ")"]),
                         ["sin", "(", "x", ")"])

    def to_expression_list(self):
        self.assertEqual(pro.to_expression_list("tan(x)"),
                         ["tan", "(", "x", ")"])
        self.assertEqual(pro.to_expression_list("-2"),
                         ["neg", "2"])

    def test_infix_to_postfix(self):
        self.assertEqual(pro.infix_to_postfix(["1", "+", "2"]),
                         ["1", "2", "+"])
        self.assertEqual(pro.infix_to_postfix(["1.0", "-", "2.5"]),
                         ["1.0", "2.5", "-"])
        self.assertEqual(pro.infix_to_postfix(["1", "*", "2"]),
                         ["1", "2", "*"])
        self.assertEqual(pro.infix_to_postfix(["1", "/", "2"]),
                         ["1", "2", "/"])
        self.assertEqual(pro.infix_to_postfix(["1", "^", "2"]),
                         ["1", "2", "^"])
        self.assertEqual(pro.infix_to_postfix(["sin", "20"]),
                         ["20", "sin"])

    def test_evaluate_postfix(self):
        self.assertEqual(pro.evaluate_postfix(["1", "2", "+"]), "3")
        self.assertEqual(pro.evaluate_postfix(["1.0", "2.5", "-"]), "-1.5")
        self.assertEqual(pro.evaluate_postfix(["1", "2", "*"]), "2")
        self.assertEqual(pro.evaluate_postfix(["1", "2", "/"]), "0.5")
        self.assertEqual(pro.evaluate_postfix(["pi", "6", "*"]),
                         "18.8495559215")
        self.assertEqual(pro.evaluate_postfix(["7.25", "floor"]), "7.0")
        self.assertEqual(pro.evaluate_postfix(["7.25", "ceil"]), "8.0")
        self.assertEqual(pro.evaluate_postfix(["20", "cos"]), "0.408082061813")
        self.assertEqual(pro.evaluate_postfix(["20", "tan"]), "2.23716094422")
        self.assertEqual(pro.evaluate_postfix(["1", "0", "/"]),
                         "Divide by zero error")
        self.assertEqual(pro.evaluate_postfix(["1", "asin"]), "1.57079632679")
        self.assertEqual(pro.evaluate_postfix(["10", "asin"]), "Domain error")
        self.assertEqual(pro.evaluate_postfix(["-1", "acos"]), "3.14159265359")
        self.assertEqual(pro.evaluate_postfix(["10", "acos"]), "Domain error")
        self.assertEqual(pro.evaluate_postfix(["-1", "atan"]),
                         "-0.785398163397")
        self.assertEqual(pro.evaluate_postfix(["3", "sinh"]), "10.0178749274")
        self.assertEqual(pro.evaluate_postfix(["3", "cosh"]), "10.0676619958")
        self.assertEqual(pro.evaluate_postfix(["3000", "cosh"]),
                         "Out of range")
        self.assertEqual(pro.evaluate_postfix(["3", "tanh"]), "0.995054753687")
        self.assertEqual(pro.evaluate_postfix(["0.5", "asinh"]),
                         "0.48121182506")
        self.assertEqual(pro.evaluate_postfix(["1.4", "acosh"]),
                         "0.867014726491")
        self.assertEqual(pro.evaluate_postfix(["-1", "acosh"]), "Domain error")
        self.assertEqual(pro.evaluate_postfix(["0.5", "atanh"]),
                         "0.549306144334")

    def test_string_to_num(self):
        self.assertEqual(pro.string_to_num("1"), 1)
        self.assertEqual(pro.string_to_num("1.0"), 1.0)

    def test_evaluate_binary_expression(self):
        self.assertEqual(pro.evaluate_binary_expression("1", "/", "2"), 0.5)
        self.assertEqual(pro.evaluate_binary_expression("1", "*", "2"), 2)

    def test_evaluate_unary_expression(self):
        self.assertEqual(pro.evaluate_unary_expression("sinh", "2.5"),
                         6.0502044810397875)

        self.assertEqual(pro.evaluate_unary_expression("floor", "2.2"), 2.0)
        self.assertEqual(pro.evaluate_unary_expression("ceil", "2.2"), 3.0)
        self.assertEqual(pro.evaluate_unary_expression("abs", "-2"), 2)

        self.assertEqual(pro.evaluate_unary_expression("sqrt", "2"),
                         1.4142135623730951)
        self.assertEqual(pro.evaluate_unary_expression("log", "10"), 1)
        self.assertEqual(pro.evaluate_unary_expression("ln", "10"),
                         2.3978952727983707)

    def is_valid(self, expression):
        valid_a = pro.valid_arithmatic_expression(expression)
        valid_p = pro.valid_arithmatic_expression(expression)

        if not (valid_a and valid_p):
            return False
        return True

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProcessing)
    unittest.TextTestRunner(verbosity=2).run(suite)
