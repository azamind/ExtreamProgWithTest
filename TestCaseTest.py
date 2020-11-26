from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(TestCase):

    def __init__(self, run_method_name):
        super().__init__(run_method_name)

    def set_up(self):
        self.result = TestResult()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert ("SetUp test_method tear_down " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert ("1 run, 0 failed" == self.result.summary())

    def test_failed_result(self):
        test = WasRun("")
        test.run(self.result)
        assert ("1 run, 1 failed" == self.result.summary())

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert ("1 run, 1 failed" == self.result.summary())
