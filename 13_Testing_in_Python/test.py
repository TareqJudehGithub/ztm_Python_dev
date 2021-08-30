import unittest


# function to test
def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please enter a number'

    except ValueError as err:
        return err

    except AssertionError as err:
        print('Values are not equal.')
        return err


# How unittest works, is that we create a class and inherit it unittest module
class TestMain(unittest.TestCase):
    # setup() enables us to include a message before each test execution.
    def setUp(self) -> None:
        print('About to run a function test..')

    test_param = int(input('Enter a value: '))

    def test_result(self):
        """Test output"""
        result = do_stuff(self.test_param)
        # assertEqual test if both test param and ours are equal
        # suppose test_param was 5, result = 10 (5+5) comparing to a test input
        self.assertEqual(result, 10)

    def test_result2(self):
        """Test output2"""
        input_2 = self.test_param
        result = do_stuff(input_2)
        self.assertEqual(result, 10)

    # teadDown() is used for more complex testing like databases.
    def tearDown(self) -> None:
        print('Cleaning up..')
    # inserting a wrong value to c if the test fails
    # def test_input_value(self):
    #
    #     result = do_stuff(self.test_param)
    #     self.assertIsInstance(result, ValueError)
    #
    #
    # def another_none(self):
    #
    #     result = do_stuff(None)
    #     self.assertIsInstance(result, 'Please enter a number')
    #
    # def test_zero(self):
    #     result = do_stuff(self.test_param)
    #     self.assertFalse(result, 0)


if __name__ == "__main__":
    unittest.main()




