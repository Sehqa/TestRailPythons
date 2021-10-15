from random import randint


class TestSuite(object):

    def __init__(self):
        self.number = randint(1, 5000)
        self.name = "b.ivanov Suite_" + str(self.number)
        self.description = "Auto_" + str(self.number)
        self.suite_id = 0
