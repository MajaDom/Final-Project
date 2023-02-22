# This class is used to raise an exception when a client with a given id does not exist in the database.
class ClientWithIdDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


# > This class is used to raise an exception when a contract is not found
class ContractNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


# It creates a new exception class called InvalidInputException.
class InvalidInputException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
