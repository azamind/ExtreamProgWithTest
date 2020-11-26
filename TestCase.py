class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        #result.testStarted()
        self.set_up()
        exec("self." + self.name + "()")
        self.tear_down()

    def tear_down(self):
        pass
