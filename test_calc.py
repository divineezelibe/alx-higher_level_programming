#!/usr/bin/python3

import unittest
import calculator

class TestCalcu(unittest.TestCase):
    
    def test_add(self):
        cal_ob=calculator.CalculateIt()
        result=cal_ob.add(2,3)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
