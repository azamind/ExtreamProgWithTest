from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):

    def __init__(self, name):
        super().__init__(name)

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        if "SetUp test_method tear_down " == test.log:
            return True
        return False
