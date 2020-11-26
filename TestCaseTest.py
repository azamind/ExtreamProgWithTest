from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):

    def __init__(self):
        super().__init__('')

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert ("SetUp test_method tear_down " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert ("1 run, 1 failed" == result.summary())
