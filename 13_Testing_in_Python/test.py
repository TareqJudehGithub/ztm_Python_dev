import unittest


# function to test
def do_stuff(num):
    try:
        return int(num) + 5

    except ValueError as err:
        print("Please enter integers only")
        return err


# How unittest works, is that we create a class and inherit it unittest module
class TestMain(unittest.TestCase):
    test_param = int(input('Enter a value: '))

    def test_result(self):

        result = do_stuff(self.test_param)
        # assertEqual test if both test param and ours are equal
        # suppose test_param was 5, result = 10 (5+5) comparing to a test input
        self.assertEqual(result, 10)

    # inserting a wrong value to c if the test fails
    # def test_input_value(self):
    #
    #     result = do_stuff(self.test_param)
    #     self.assertIsInstance(result, ValueError)
    #

unittest.main()




