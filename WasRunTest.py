from pprint import pprint

from TestCaseTest import TestCaseTest
from WasRun import WasRun

test = WasRun("test_method")
pprint(test.log)
test.run()
pprint(test.log)

pprint(TestCaseTest("test_result").run().summary())
pprint(TestCaseTest("test_template_method").run().summary())
pprint(TestCaseTest("test_failed_result").run().summary())
pprint(TestCaseTest("test_failed_result_formatting").run().summary())
