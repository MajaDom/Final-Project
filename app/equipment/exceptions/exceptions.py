class EquipmentDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class AssignedEquipmentDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidInputException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class EquipmentHasBeenAssignedException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
