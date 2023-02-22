# This class is a custom exception class that is used to raise an exception when a cost center is not found
class CostCenterNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
