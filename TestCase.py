from TestResult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            exec("self." + self.name + "()")
        except Exception:
            result.test_failed()
        self.tear_down()
        return result
