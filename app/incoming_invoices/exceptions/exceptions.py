# This class is used to raise an exception when the incoming invoice does not exist in the database.
class IncomingInvoiceDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class IncomingInvoicePaymentDoesNotExistInTheDatabaseException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidInputException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code
