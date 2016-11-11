#!/usr/bin/env python

import app.calculator.processing as pro
import unittest

class TestProcessing(unittest.TestCase):

    def test_infix_to_postfix(self):
        self.assertEqual(pro.infix_to_postfix(["1", "+", "2"]), ["1", "2", "+"])
    
if __name__ == "__main__":
    unittest.main()
