# This class is used to raise an exception when a user is not found in the database.
class UserNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserMissingDataException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserInvalidPassword(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeMissingDataException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class NoActiveContractsForEmployeeException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class NoContractsForEmployeeException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidInputException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeInactiveException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class ExistingActiveContractException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
