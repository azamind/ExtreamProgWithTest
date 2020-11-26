from TestCaseTest import TestCaseTest
from TestResult import TestResult
from TestSuite import TestSuite

suite = TestSuite()
suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_failed_result_formatting"))

result = TestResult()
suite.run(result)
print(result.summary())
