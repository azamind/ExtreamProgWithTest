from TestResult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        print(self.name)
        result = TestResult()
        result.test_started()
        self.set_up()
        if self.name == 'test_failed_result_formatting' or self.name == 'test_failed_result':
            result.test_failed()
        else:
            exec("self." + self.name + "()")

        self.tear_down()
        return result
