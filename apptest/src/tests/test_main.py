# Test cases will be added here
import unittest
# from src.main import some_function_to_test # Example

class TestMain(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1 + 1, 2)

    # def test_some_functionality(self):
    #     # Add actual tests here
    #     pass

if __name__ == '__main__':
    unittest.main()