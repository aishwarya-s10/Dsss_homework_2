import unittest
from math_quiz import Generate_Random_Integer, Get_Random_Operator, Generate_Mathematical_Expression_Result


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Generate_Random_Integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the random operator is one of the expected operators
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operators
            rand_operator = Get_Random_Operator()
            self.assertTrue(rand_operator in operators)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 4, '-', '10 - 4', 6),
                (3, 6, '*', '3 * 6', 18)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_mathematical_expression_result(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
