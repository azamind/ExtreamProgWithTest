class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def test_started(self):
        self.runCount += 1

    def test_failed(self):
        self.errorCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)
