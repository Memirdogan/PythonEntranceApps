
# DO NOT ALTER OR CHANGE ANY LINES IN THIS FILE.

# STUDENTS ARE ONLY RESPONSIBLE FOR RECTANGLE.PY FILE THAT IS IMPORTED BELOW.

from Rectangle import *

import unittest
from unittest.mock import patch
from io import StringIO
import inspect

def score(value):
    def decorator(func):
        func.score = value
        return func
    return decorator

class ScoringTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_score = 0
        self.max_score = 0

    def startTest(self, test):
        super().startTest(test)
        test_method = getattr(test, test._testMethodName)
        self.current_test_score = getattr(test_method, 'score', 0)
        self.max_score += self.current_test_score

    def addSuccess(self, test: unittest.TestCase) -> None:
        super().addSuccess(test)
        self.total_score += self.current_test_score

    def addFailure(self, test, err):
        super().addFailure(test, err)

    def addError(self, test, err):
        super().addError(test, err)

    def getScore(self):
        return (self.total_score, self.max_score)
    
class ScoringTestRunner(unittest.TextTestRunner):
    resultclass = ScoringTestResult
    
    def run(self, test):
        result = super().run(test)
        total_score, max_score = result.getScore()
        #print(f"\nTotal Score: {total_score}/{max_score}")
        return result


class TestRectangle(unittest.TestCase):
    @score(4)
    def test_valid_rectangle(self):
        r = Rectangle([50, 50], 200, 200)
        self.assertEqual(r.xlength, 200)
        self.assertEqual(r.ylength, 200)
        self.assertEqual(r.topleft, [50, 50])
        self.assertEqual(r.area(), 40000)
        

    @score(4)
    def test_invalid_xlength(self):
        r = Rectangle([50, 50], -200, 200)
        self.assertIsNone(r.xlength)
        self.assertIsNone(r.ylength)
        self.assertIsNone(r.topleft)

    @score(4)
    def test_invalid_ylength(self):
        r = Rectangle([50, 50], 200, 0)
        self.assertIsNone(r.xlength)
        self.assertIsNone(r.ylength)
        self.assertIsNone(r.topleft)

    @score(4)
    def test_invalid_both_lengths(self):
        r = Rectangle([50, 50], -50, -100)
        self.assertIsNone(r.xlength)
        self.assertIsNone(r.ylength)
        self.assertIsNone(r.topleft)
    
    
    @patch('sys.stdout', new_callable=StringIO)
    @score(4)   
    def  test_print_message(self, mock_stdout):
        r = Rectangle([2, 3], -5, -10)
        self.assertIn("Specified rectangle cannot be created!!!", mock_stdout.getvalue())
    
    @score(10)  
    def test_intersect_DoesIntersect(self):
        rectangle_A = Rectangle([200,200], 100, 100)
        rectangle_B = Rectangle([250,250], 300, 300)
        self.assertTrue(rectangle_A.intersect(rectangle_B))
       
        rectangle_A = Rectangle([100,100], 50, 100)
        rectangle_B = Rectangle([90,150], 35, 100)
        self.assertTrue(rectangle_A.intersect(rectangle_B))
        
        rectangle_A = Rectangle([20,20], 5, 10)
        rectangle_B = Rectangle([5,30], 55, 30)
        self.assertTrue(rectangle_A.intersect(rectangle_B))
    
    @score(10)
    def test_intersect_DoesNotIntersect(self):
        
        rectangle_A = Rectangle([20,20], 5, 10)
        rectangle_B = Rectangle([30,30], 30, 30)
        self.assertFalse(rectangle_A.intersect(rectangle_B))
        
        rectangle_A = Rectangle([20,50], 5, 15)
        rectangle_B = Rectangle([5,30], 55, 30)
        self.assertFalse(rectangle_A.intersect(rectangle_B))
            
    @score(4)
    def test_lt_signature(self):
        sig = inspect.signature(Rectangle.__lt__)
        expected_params = ['self','other']
        actual_params = list(sig.parameters.keys())
        self.assertEqual(expected_params, actual_params, f"Expected signature: {expected_params}, but got: {actual_params}")
    
    @score(8)
    def test_lt_isSmaller(self):
        rectangle_A = Rectangle([20,20], 10, 10)
        rectangle_B = Rectangle([30,30], 30, 30)
        self.assertTrue(rectangle_A < rectangle_B)
    
    @score(8)
    def test_lt_isNotSmaller(self):
        rectangle_A = Rectangle([20,20], 50, 20)
        rectangle_B = Rectangle([30,30], 30, 30)
        self.assertFalse(rectangle_A < rectangle_B)
    
    @score(4)   
    def test_distance_signature(self):
        sig = inspect.signature(Rectangle.distance)
        expected_params = ['self','other']
        actual_params = list(sig.parameters.keys())
        self.assertEqual(expected_params, actual_params, f"Expected signature: {expected_params}, but got: {actual_params}")
    
    @score(16)   
    def test_distance(self):
        rectangle_A = Rectangle([-5,35], 10, 10)
        rectangle_B = Rectangle([35,5], 10, 10)
        self.assertTrue(abs(rectangle_A.distance(rectangle_B) - 50) < 1e-3)

    @score(4)   
    def test_generate_adjacent_signature(self):
        sig = inspect.signature(Rectangle.generate_adjacent)
        expected_params = ['self','side']
        actual_params = list(sig.parameters.keys())
        self.assertEqual(expected_params, actual_params, f"Expected signature: {expected_params}, but got: {actual_params}")

    
    @score(8)    
    def test_generate_adjacent_returnsRectangle(self):
        rectangle_A = Rectangle([10,10], 10, 10)
        adj_rect_right = rectangle_A.generate_adjacent(side='right')
        adj_rect_left = rectangle_A.generate_adjacent(side='left')
        adj_rect_above = rectangle_A.generate_adjacent(side='above')
        adj_rect_below = rectangle_A.generate_adjacent(side='below')
        
        self.assertTrue(isinstance(adj_rect_right, Rectangle))
        self.assertTrue(isinstance(adj_rect_left, Rectangle))
        self.assertTrue(isinstance(adj_rect_above, Rectangle))
        self.assertTrue(isinstance(adj_rect_below, Rectangle))
        
    @score(8)    
    def test_generate_adjacent_only_rightleftabovebelow(self):
        rectangle_A = Rectangle([10,10], 10, 10)
        adj_rect = rectangle_A.generate_adjacent(side='under')
        
        self.assertIsNone(adj_rect)      
        
            

if __name__ == '__main__':
    
    suite = unittest.TestSuite()
    suite.addTest(TestRectangle('test_valid_rectangle'))
    suite.addTest(TestRectangle('test_invalid_xlength'))
    suite.addTest(TestRectangle('test_invalid_ylength'))
    suite.addTest(TestRectangle('test_invalid_both_lengths'))
    suite.addTest(TestRectangle('test_print_message'))
    suite.addTest(TestRectangle('test_intersect_DoesIntersect'))
    suite.addTest(TestRectangle('test_intersect_DoesNotIntersect'))
    suite.addTest(TestRectangle('test_lt_signature'))
    suite.addTest(TestRectangle('test_lt_isSmaller'))
    suite.addTest(TestRectangle('test_lt_isNotSmaller'))
    suite.addTest(TestRectangle('test_distance_signature'))
    suite.addTest(TestRectangle('test_distance'))
    suite.addTest(TestRectangle('test_generate_adjacent_signature'))
    suite.addTest(TestRectangle('test_generate_adjacent_returnsRectangle'))
    suite.addTest(TestRectangle('test_generate_adjacent_only_rightleftabovebelow'))
    
    runner = ScoringTestRunner(verbosity=2)
    result = runner.run(suite)
    score, max_score = result.getScore()
    print()
    print(f"\nFunctionality (Correctness) Score: {score}/{max_score}")
    print()
