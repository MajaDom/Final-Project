class UserNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserMissingDataException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code