from random import randint
from const_for_test_rail import *


class TestRun(object):
    def __init__(self):
        self.number = randint(1, 5000)
        self.name = "b.ivanov Run_" + str(self.number)
        self.description = "Auto_Run_" + str(self.number)
        self.project_id = PROJECT_ID
        self.run_id = 0
