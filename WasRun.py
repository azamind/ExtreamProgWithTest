from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        self.was_set_up = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.was_run = 1

    def set_up(self):
        self.was_run = None
        self.was_set_up = 1
