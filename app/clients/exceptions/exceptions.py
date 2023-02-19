class ClientWithIdDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class ContractNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidInputException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
