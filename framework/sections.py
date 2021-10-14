from random import randint


class Sections(object):

    def __init__(self, suite_id):
        self.number = randint(1, 5000)
        self.name = "b.ivanov Sections_" + str(self.number)
        self.description = "Auto_" + str(self.number)
        self.suite_id = suite_id
        self.section_id = 0
