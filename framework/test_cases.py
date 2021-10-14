from random import randint


class TestCase(object):

    def __init__(self):
        self.number = randint(1, 5000)
        self.title = "Auto_" + str(self.number)
        self.section_id = 0
        self.case_id = 0
        self.template_id = 1
