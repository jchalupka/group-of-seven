#!/usr/bin/env python

import app.calculator.processing as pro
import unittest


class TestProcessing(unittest.TestCase):


    in_func = ["sin", "20"]
    post_func = ["20", "sin"]

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
        self.assertEqual(pro.evaluate_postfix(["20", "sin"]), "0.342020143326")
        self.assertEqual(pro.evaluate_postfix(["1", "0", "/"]), "Divide by zero")

    def test_string_to_num(self):
        self.assertEqual(pro.string_to_num("1"), 1)
        self.assertEqual(pro.string_to_num("1.0"), 1.0)

    def test_divide(self):
        self.assertEqual(pro.divide(1, 2), 0.5)
        self.assertEqual(pro.divide(1, 0), "Divide by zero")

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

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProcessing)
    unittest.TextTestRunner(verbosity=2).run(suite)
