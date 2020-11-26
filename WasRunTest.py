from pprint import pprint

from TestCaseTest import TestCaseTest
from WasRun import WasRun

test = WasRun("test_method")
pprint(test.log)
test.run()
pprint(test.log)

test_case_test = TestCaseTest()
pprint(test_case_test.test_template_method())
pprint(test_case_test.test_result())
pprint(test_case_test.test_failed_result())
