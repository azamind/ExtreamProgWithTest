from TestCase import TestCase


class WasRun(TestCase):
    log: str
    was_run: None
    was_set_up: None

    def __init__(self, name):
        super().__init__(name)
        self.log = ''
        self.was_run = None
        self.was_set_up = None

    def set_up(self):
        self.log = "SetUp "

    def test_method(self):
        self.log = self.log + "test_method "

    def tear_down(self):
        self.log = self.log + "tear_down "
