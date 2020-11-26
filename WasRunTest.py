from pprint import pprint

from TestCaseTest import TestCaseTest
from WasRun import WasRun

test = WasRun("test_method")
pprint(test.log)
test.run()
pprint(test.log)

test2 = TestCaseTest("test_method")
pprint(test2.test_template_method())
